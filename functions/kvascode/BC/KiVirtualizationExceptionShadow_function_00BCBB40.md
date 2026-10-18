# KiVirtualizationExceptionShadow

- RVA: `0x00BCBB40`–`0x00BCBBB7` (길이 `119` bytes)
- VA: `0x0000000140BCBB40`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C190C`
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
  - `0x00BCBBA9` → [KiVirtualizationException](../../text/6C/KiVirtualizationException_function_006C2900.md) (`tail-transfer`)
  - `0x00BCBBB1` → [KiVirtualizationException](../../text/6C/KiVirtualizationException_function_006C2900.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCBB40  F6 44 24 08 01                  test byte ptr [rsp + 8], 1
00BCBB45  74 67                           je 0x140bcbbae
00BCBB47  0F 01 F8                        swapgs
00BCBB4A  0F AE E8                        lfence
00BCBB4D  65 0F BA 24 25 18 B0 00 00 01   bt dword ptr gs:[0xb018], 1
00BCBB57  72 0C                           jb 0x140bcbb65
00BCBB59  65 48 8B 24 25 00 B0 00 00      mov rsp, qword ptr gs:[0xb000]
00BCBB62  0F 22 DC                        mov cr3, rsp
00BCBB65  65 48 8B 24 25 08 B0 00 00      mov rsp, qword ptr gs:[0xb008]
00BCBB6E  65 48 89 34 25 10 00 00 00      mov qword ptr gs:[0x10], rsi
00BCBB77  65 48 8B 34 25 38 00 00 00      mov rsi, qword ptr gs:[0x38]
00BCBB80  48 81 C6 00 42 00 00            add rsi, 0x4200
00BCBB87  FF 76 F8                        push qword ptr [rsi - 8]
00BCBB8A  FF 76 F0                        push qword ptr [rsi - 0x10]
00BCBB8D  FF 76 E8                        push qword ptr [rsi - 0x18]
00BCBB90  FF 76 E0                        push qword ptr [rsi - 0x20]
00BCBB93  FF 76 D8                        push qword ptr [rsi - 0x28]
00BCBB96  65 48 8B 34 25 10 00 00 00      mov rsi, qword ptr gs:[0x10]
00BCBB9F  65 48 83 24 25 10 00 00 00 00   and qword ptr gs:[0x10], 0
00BCBBA9  E9 52 6D AF FF                  jmp 0x1406c2900
00BCBBAE  0F AE E8                        lfence
00BCBBB1  E9 4A 6D AF FF                  jmp 0x1406c2900
00BCBBB6  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiVirtualizationExceptionShadow(void)
{
    __int64 v_cr3;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_p8;

    if (((v_stack_p8) & (1)) == 0) goto loc_00BCBBAE;
    if (!(condition_is_below)) {
        v_rsp = *(unsigned __int64 *)(gs_base + (0 + 45056));
        v_cr3 = v_rsp;
    }
    *(unsigned __int64 *)(gs_base + (0 + 16)) = v_rsi;
    v_rsi = (*(unsigned __int64 *)(gs_base + (0 + 56))) + (0x4200ULL);
loc_00BCBBAE:
}
```

## 5. (Beta) C Style

```c
void KiVirtualizationExceptionShadow(void)
{
    int64_t v_cr3;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_p8;

    if (((v_stack_p8) & (1)) == 0) goto loc_00BCBBAE;
    if (!(condition_is_below)) {
        local_rsp = *(uint64_t *)(gs_base + (0 + 0xB000));
        v_cr3 = local_rsp;
    }
    *(uint64_t *)(gs_base + (0 + 0x10)) = local_rsi;
    local_rsi = (*(uint64_t *)(gs_base + (0 + 0x38))) + (0x4200ULL);
loc_00BCBBAE:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCBB40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCBB40[BB_00BCBB40]
  bb_00BCBB47[BB_00BCBB47]
  bb_00BCBB59[BB_00BCBB59]
  bb_00BCBB65[BB_00BCBB65]
  bb_00BCBBAE[BB_00BCBBAE]
  bb_00BCBBB6[BB_00BCBBB6]
  bb_00BCBB40 -->|branch| bb_00BCBBAE
  bb_00BCBB40 -->|fallthrough| bb_00BCBB47
  bb_00BCBB47 -->|branch| bb_00BCBB65
  bb_00BCBB47 -->|fallthrough| bb_00BCBB59
  bb_00BCBB59 -->|flow| bb_00BCBB65
```
