# HalpBlkWdTimerRoutine

- RVA: `0x0056E7D0`–`0x0056E800` (길이 `48` bytes)
- VA: `0x000000014056E7D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0056E7F5` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0056E7D4` → RVA `0x00F8FA90` (`.data`; read)
- `0x0056E7E4` → RVA `0x00F8F888` (`.data`; read/write)
- `0x0056E7EE` → RVA `0x00F8F7E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056E7D0  48 83 EC 28                     sub rsp, 0x28
0056E7D4  83 3D B5 12 A2 00 00            cmp dword ptr [rip + 0xa212b5], 0
0056E7DB  74 1D                           je 0x14056e7fa
0056E7DD  BA 01 00 00 00                  mov edx, 1
0056E7E2  8B C2                           mov eax, edx
0056E7E4  87 05 9E 10 A2 00               xchg dword ptr [rip + 0xa2109e], eax
0056E7EA  85 C0                           test eax, eax
0056E7EC  75 0C                           jne 0x14056e7fa
0056E7EE  48 8D 0D EB 0F A2 00            lea rcx, [rip + 0xa20feb]
0056E7F5  E8 26 AD D8 FF                  call 0x1402f9520
0056E7FA  48 83 C4 28                     add rsp, 0x28
0056E7FE  C3                              ret
0056E7FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBlkWdTimerRoutine(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 10621621)) == 0) goto loc_0056E7FA;
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 10620907;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpBlkWdTimerRoutine(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0xA212B5)) == 0) goto loc_0056E7FA;
    result = 1;
    if (1 == 0) {
        a1 = v_rip + 10620907;
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056E7D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056E7D0[BB_0056E7D0]
  bb_0056E7DD[BB_0056E7DD]
  bb_0056E7EE[BB_0056E7EE]
  bb_0056E7FA[BB_0056E7FA]
  bb_0056E7FF[BB_0056E7FF]
  bb_0056E7D0 -->|branch| bb_0056E7FA
  bb_0056E7D0 -->|fallthrough| bb_0056E7DD
  bb_0056E7DD -->|branch| bb_0056E7FA
  bb_0056E7DD -->|fallthrough| bb_0056E7EE
  bb_0056E7EE -->|flow| bb_0056E7FA
```
