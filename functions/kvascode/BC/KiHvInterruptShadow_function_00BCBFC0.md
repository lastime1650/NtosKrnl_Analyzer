# KiHvInterruptShadow

- RVA: `0x00BCBFC0`–`0x00BCC037` (길이 `119` bytes)
- VA: `0x0000000140BCBFC0`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1978`
- 디코드: `23`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00BCC029` → [KiHvInterrupt](../../text/6B/KiHvInterrupt_function_006B6620.md) (`tail-transfer`)
  - `0x00BCC031` → [KiHvInterrupt](../../text/6B/KiHvInterrupt_function_006B6620.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCBFC0  F6 44 24 08 01                  test byte ptr [rsp + 8], 1
00BCBFC5  74 67                           je 0x140bcc02e
00BCBFC7  0F 01 F8                        swapgs
00BCBFCA  0F AE E8                        lfence
00BCBFCD  65 0F BA 24 25 18 B0 00 00 01   bt dword ptr gs:[0xb018], 1
00BCBFD7  72 0C                           jb 0x140bcbfe5
00BCBFD9  65 48 8B 24 25 00 B0 00 00      mov rsp, qword ptr gs:[0xb000]
00BCBFE2  0F 22 DC                        mov cr3, rsp
00BCBFE5  65 48 8B 24 25 08 B0 00 00      mov rsp, qword ptr gs:[0xb008]
00BCBFEE  65 48 89 34 25 10 00 00 00      mov qword ptr gs:[0x10], rsi
00BCBFF7  65 48 8B 34 25 38 00 00 00      mov rsi, qword ptr gs:[0x38]
00BCC000  48 81 C6 00 42 00 00            add rsi, 0x4200
00BCC007  FF 76 F8                        push qword ptr [rsi - 8]
00BCC00A  FF 76 F0                        push qword ptr [rsi - 0x10]
00BCC00D  FF 76 E8                        push qword ptr [rsi - 0x18]
00BCC010  FF 76 E0                        push qword ptr [rsi - 0x20]
00BCC013  FF 76 D8                        push qword ptr [rsi - 0x28]
00BCC016  65 48 8B 34 25 10 00 00 00      mov rsi, qword ptr gs:[0x10]
00BCC01F  65 48 83 24 25 10 00 00 00 00   and qword ptr gs:[0x10], 0
00BCC029  E9 F2 A5 AE FF                  jmp 0x1406b6620
00BCC02E  0F AE E8                        lfence
00BCC031  E9 EA A5 AE FF                  jmp 0x1406b6620
00BCC036  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiHvInterruptShadow(void)
{
    __int64 v_cr3;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_p8;

    if (((v_stack_p8) & (1)) == 0) goto loc_00BCC02E;
    if (!(condition_is_below)) {
        v_rsp = *(unsigned __int64 *)(gs_base + (0 + 45056));
        v_cr3 = v_rsp;
    }
    *(unsigned __int64 *)(gs_base + (0 + 16)) = v_rsi;
    v_rsi = (*(unsigned __int64 *)(gs_base + (0 + 56))) + (0x4200ULL);
loc_00BCC02E:
}
```

## 5. (Beta) C Style

```c
void KiHvInterruptShadow(void)
{
    int64_t v_cr3;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_p8;

    if (((v_stack_p8) & (1)) == 0) goto loc_00BCC02E;
    if (!(condition_is_below)) {
        local_rsp = *(uint64_t *)(gs_base + (0 + 0xB000));
        v_cr3 = local_rsp;
    }
    *(uint64_t *)(gs_base + (0 + 0x10)) = local_rsi;
    local_rsi = (*(uint64_t *)(gs_base + (0 + 0x38))) + (0x4200ULL);
loc_00BCC02E:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCBFC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCBFC0[BB_00BCBFC0]
  bb_00BCBFC7[BB_00BCBFC7]
  bb_00BCBFD9[BB_00BCBFD9]
  bb_00BCBFE5[BB_00BCBFE5]
  bb_00BCC02E[BB_00BCC02E]
  bb_00BCC036[BB_00BCC036]
  bb_00BCBFC0 -->|branch| bb_00BCC02E
  bb_00BCBFC0 -->|fallthrough| bb_00BCBFC7
  bb_00BCBFC7 -->|branch| bb_00BCBFE5
  bb_00BCBFC7 -->|fallthrough| bb_00BCBFD9
  bb_00BCBFD9 -->|flow| bb_00BCBFE5
```
