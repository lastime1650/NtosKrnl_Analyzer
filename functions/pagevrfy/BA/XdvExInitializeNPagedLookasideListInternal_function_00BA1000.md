# XdvExInitializeNPagedLookasideListInternal

- RVA: `0x00BA1000`–`0x00BA104C` (길이 `76` bytes)
- VA: `0x0000000140BA1000`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `15`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA1041` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA1041` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA1000  48 8B C4                        mov rax, rsp
00BA1003  48 83 EC 58                     sub rsp, 0x58
00BA1007  44 8B 94 24 98 00 00 00         mov r10d, dword ptr [rsp + 0x98]
00BA100F  44 89 50 E0                     mov dword ptr [rax - 0x20], r10d
00BA1013  44 0F B7 94 24 90 00 00 00      movzx r10d, word ptr [rsp + 0x90]
00BA101C  66 44 89 50 D8                  mov word ptr [rax - 0x28], r10w
00BA1021  44 8B 94 24 88 00 00 00         mov r10d, dword ptr [rsp + 0x88]
00BA1029  44 89 50 D0                     mov dword ptr [rax - 0x30], r10d
00BA102D  4C 8B 94 24 80 00 00 00         mov r10, qword ptr [rsp + 0x80]
00BA1035  4C 89 50 C8                     mov qword ptr [rax - 0x38], r10
00BA1039  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
00BA1041  E8 8A 9A B1 FF                  call 0x1406baad0
00BA1046  48 83 C4 58                     add rsp, 0x58
00BA104A  C3                              ret
00BA104B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XdvExInitializeNPagedLookasideListInternal(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned __int16 a7, unsigned int a8, __int64 a9)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (88);
    *(unsigned int *)(v_rsp - 32) = (unsigned int)((unsigned int)(a8));
    *(unsigned __int16 *)(v_rsp - 40) = a7;
    *(unsigned int *)(v_rsp - 48) = (unsigned int)((unsigned int)(a6));
    *(unsigned __int64 *)(v_rsp - 56) = a5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XdvExInitializeNPagedLookasideListInternal(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint16_t Arg7, uint32_t Arg8, int64_t Arg9)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (88);
    *(uint32_t *)(local_rsp - 0x20) = (uint32_t)((uint32_t)(Arg8));
    *(uint16_t *)(local_rsp - 0x28) = Arg7;
    *(uint32_t *)(local_rsp - 0x30) = (uint32_t)((uint32_t)(Arg6));
    *(uint64_t *)(local_rsp - 0x38) = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA1000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA1000[BB_00BA1000]
  bb_00BA104B[BB_00BA104B]
```
