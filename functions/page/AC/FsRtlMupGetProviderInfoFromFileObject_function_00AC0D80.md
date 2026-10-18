# FsRtlMupGetProviderInfoFromFileObject

- RVA: `0x00AC0D80`–`0x00AC0DA5` (길이 `37` bytes)
- VA: `0x0000000140AC0D80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AC0D93` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AC0D84` → RVA `0x00FD8128` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AC0D93` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC0D80  48 83 EC 38                     sub rsp, 0x38
00AC0D84  48 8B 05 9D 73 51 00            mov rax, qword ptr [rip + 0x51739d]
00AC0D8B  48 85 C0                        test rax, rax
00AC0D8E  74 0E                           je 0x140ac0d9e
00AC0D90  48 8B 00                        mov rax, qword ptr [rax]
00AC0D93  E8 38 9D BF FF                  call 0x1406baad0
00AC0D98  48 83 C4 38                     add rsp, 0x38
00AC0D9C  C3                              ret
00AC0D9D  CC                              int3
00AC0D9E  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00AC0DA3  EB F3                           jmp 0x140ac0d98
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlMupGetProviderInfoFromFileObject(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (*(unsigned __int64 *)(v_rip + 5338013) == 0) goto loc_00AC0D9E;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00AC0D98:
    v_rsp = (v_rsp) + (56);
    return result;
loc_00AC0D9E:
    goto loc_00AC0D98;
}
```

## 5. (Beta) C Style

```c
void FsRtlMupGetProviderInfoFromFileObject(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (*(uint64_t *)(v_rip + 0x51739D) == 0) goto loc_00AC0D9E;
    result = guard_dispatch_icall(a1, a2, a3, a4);
loc_00AC0D98:
    local_rsp = (local_rsp) + (56);
    return result;
loc_00AC0D9E:
    goto loc_00AC0D98;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC0D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC0D80[BB_00AC0D80]
  bb_00AC0D90[BB_00AC0D90]
  bb_00AC0D98[BB_00AC0D98]
  bb_00AC0D9D[BB_00AC0D9D]
  bb_00AC0D9E[BB_00AC0D9E]
  bb_00AC0D80 -->|branch| bb_00AC0D9E
  bb_00AC0D80 -->|fallthrough| bb_00AC0D90
  bb_00AC0D90 -->|flow| bb_00AC0D98
  bb_00AC0D9D -->|flow| bb_00AC0D9E
  bb_00AC0D9E -->|branch| bb_00AC0D98
```
