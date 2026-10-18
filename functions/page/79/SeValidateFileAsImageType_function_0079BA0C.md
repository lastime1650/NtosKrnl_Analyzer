# SeValidateFileAsImageType

- RVA: `0x0079BA0C`–`0x0079BA2E` (길이 `34` bytes)
- VA: `0x000000014079BA0C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0079BA23` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ExpQueryElamCertInfo](../7C/ExpQueryElamCertInfo_function_007C4564.md) at `0x007C473C`
- [ExpQueryElamCertInfo](../7C/ExpQueryElamCertInfo_function_007C4564.md) at `0x007C478E`
- [sub_00B4433C](../B4/Unknown_function_00B4433C.md) at `0x00B44414`

### Static image references
- `0x0079BA10` → RVA `0x00F04E88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0079BA23` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079BA0C  48 83 EC 28                     sub rsp, 0x28
0079BA10  48 8B 05 71 94 76 00            mov rax, qword ptr [rip + 0x769471]
0079BA17  48 85 C0                        test rax, rax
0079BA1A  75 07                           jne 0x14079ba23
0079BA1C  B8 BB 00 00 C0                  mov eax, 0xc00000bb
0079BA21  EB 05                           jmp 0x14079ba28
0079BA23  E8 A8 F0 F1 FF                  call 0x1406baad0
0079BA28  48 83 C4 28                     add rsp, 0x28
0079BA2C  C3                              ret
0079BA2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeValidateFileAsImageType(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 7771249) != 0) goto loc_0079BA23;
    goto loc_0079BA28;
loc_0079BA23:
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_0079BA28:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SeValidateFileAsImageType(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x769471) != 0) goto loc_0079BA23;
    goto loc_0079BA28;
loc_0079BA23:
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_0079BA28:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079BA0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079BA0C[BB_0079BA0C]
  bb_0079BA1C[BB_0079BA1C]
  bb_0079BA23[BB_0079BA23]
  bb_0079BA28[BB_0079BA28]
  bb_0079BA2D[BB_0079BA2D]
  bb_0079BA0C -->|branch| bb_0079BA23
  bb_0079BA0C -->|fallthrough| bb_0079BA1C
  bb_0079BA1C -->|branch| bb_0079BA28
  bb_0079BA23 -->|flow| bb_0079BA28
```
