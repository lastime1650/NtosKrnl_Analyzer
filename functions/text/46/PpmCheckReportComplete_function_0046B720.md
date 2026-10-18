# PpmCheckReportComplete

- RVA: `0x0046B720`–`0x0046B74B` (길이 `43` bytes)
- VA: `0x000000014046B720`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0046B73E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0046B724` → RVA `0x00F0E290` (`.data`; read)
- `0x0046B730` → RVA `0x00F0B260` (`.data`; read)
- `0x0046B737` → RVA `0x00F0E260` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046B720  48 83 EC 28                     sub rsp, 0x28
0046B724  48 8B 05 65 2B AA 00            mov rax, qword ptr [rip + 0xaa2b65]
0046B72B  48 85 C0                        test rax, rax
0046B72E  74 13                           je 0x14046b743
0046B730  48 8B 15 29 FB A9 00            mov rdx, qword ptr [rip + 0xa9fb29]
0046B737  48 8B 0D 22 2B AA 00            mov rcx, qword ptr [rip + 0xaa2b22]
0046B73E  E8 8D F3 24 00                  call 0x1406baad0
0046B743  B0 01                           mov al, 1
0046B745  48 83 C4 28                     add rsp, 0x28
0046B749  C3                              ret
0046B74A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmCheckReportComplete(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(v_rip + 11152229);
    if (*(unsigned __int64 *)(v_rip + 11152229) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 11139881);
        a1 = *(unsigned __int64 *)(v_rip + 11152162);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
void PpmCheckReportComplete(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(v_rip + 0xAA2B65);
    if (*(uint64_t *)(v_rip + 0xAA2B65) != 0) {
        a2 = *(uint64_t *)(v_rip + 0xA9FB29);
        a1 = *(uint64_t *)(v_rip + 0xAA2B22);
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046B720&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046B720[BB_0046B720]
  bb_0046B730[BB_0046B730]
  bb_0046B743[BB_0046B743]
  bb_0046B74A[BB_0046B74A]
  bb_0046B720 -->|branch| bb_0046B743
  bb_0046B720 -->|fallthrough| bb_0046B730
  bb_0046B730 -->|flow| bb_0046B743
```
