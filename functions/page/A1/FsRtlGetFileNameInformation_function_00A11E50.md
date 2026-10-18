# FsRtlGetFileNameInformation

- RVA: `0x00A11E50`–`0x00A11E76` (길이 `38` bytes)
- VA: `0x0000000140A11E50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `11`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A11E64` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [EtwpCancelTraceImageUnloadApc](../../text/65/EtwpCancelTraceImageUnloadApc_function_00650810.md) at `0x00650838`

### Static image references
- `0x00A11E54` → RVA `0x00E65BF0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A11E64` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A11E50  48 83 EC 38                     sub rsp, 0x38
00A11E54  48 8B 05 95 3D 45 00            mov rax, qword ptr [rip + 0x453d95]
00A11E5B  48 85 C0                        test rax, rax
00A11E5E  74 0F                           je 0x140a11e6f
00A11E60  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00A11E64  E8 67 8C CA FF                  call 0x1406baad0
00A11E69  48 83 C4 38                     add rsp, 0x38
00A11E6D  C3                              ret
00A11E6E  CC                              int3
00A11E6F  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00A11E74  EB F3                           jmp 0x140a11e69
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlGetFileNameInformation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(v_rip + 4537749) == 0) goto loc_00A11E6F;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00A11E69:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00A11E6F:
    goto loc_00A11E69;
}
```

## 5. (Beta) C Style

```c
void FsRtlGetFileNameInformation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(v_rip + 0x453D95) == 0) goto loc_00A11E6F;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00A11E69:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00A11E6F:
    goto loc_00A11E69;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A11E50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A11E50[BB_00A11E50]
  bb_00A11E60[BB_00A11E60]
  bb_00A11E69[BB_00A11E69]
  bb_00A11E6E[BB_00A11E6E]
  bb_00A11E6F[BB_00A11E6F]
  bb_00A11E50 -->|branch| bb_00A11E6F
  bb_00A11E50 -->|fallthrough| bb_00A11E60
  bb_00A11E60 -->|flow| bb_00A11E69
  bb_00A11E6E -->|flow| bb_00A11E6F
  bb_00A11E6F -->|branch| bb_00A11E69
```
