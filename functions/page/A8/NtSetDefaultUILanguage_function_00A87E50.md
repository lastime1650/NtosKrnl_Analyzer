# NtSetDefaultUILanguage

- RVA: `0x00A87E50`–`0x00A87E68` (길이 `24` bytes)
- VA: `0x0000000140A87E50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A87E59` → [ExpSetPendingUILanguage](ExpSetPendingUILanguage_function_00A87E70.md) (function, `0x00A87E70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A87E50  48 83 EC 28                     sub rsp, 0x28
00A87E54  66 85 C9                        test cx, cx
00A87E57  75 0B                           jne 0x140a87e64
00A87E59  E8 12 00 00 00                  call 0x140a87e70
00A87E5E  48 83 C4 28                     add rsp, 0x28
00A87E62  C3                              ret
00A87E63  CC                              int3
00A87E64  33 C0                           xor eax, eax
00A87E66  EB F6                           jmp 0x140a87e5e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetDefaultUILanguage(unsigned __int16 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_00A87E64;
    result = ExpSetPendingUILanguage(a1, a2, a3, a4);
loc_00A87E5E:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A87E64:
    result = 0;
    goto loc_00A87E5E;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetDefaultUILanguage(uint16_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_00A87E64;
    result = ExpSetPendingUILanguage(Arg1, a2, a3, a4);
loc_00A87E5E:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A87E64:
    result = 0;
    goto loc_00A87E5E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A87E50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A87E50[BB_00A87E50]
  bb_00A87E59[BB_00A87E59]
  bb_00A87E5E[BB_00A87E5E]
  bb_00A87E63[BB_00A87E63]
  bb_00A87E64[BB_00A87E64]
  bb_00A87E50 -->|branch| bb_00A87E64
  bb_00A87E50 -->|fallthrough| bb_00A87E59
  bb_00A87E59 -->|flow| bb_00A87E5E
  bb_00A87E63 -->|flow| bb_00A87E64
  bb_00A87E64 -->|branch| bb_00A87E5E
```
