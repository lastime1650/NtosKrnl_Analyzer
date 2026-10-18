# NtNotifyChangeDirectoryFile

- RVA: `0x00A1DE40`–`0x00A1DE92` (길이 `82` bytes)
- VA: `0x0000000140A1DE40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `16`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A1DE87` → [NtNotifyChangeDirectoryFileEx](NtNotifyChangeDirectoryFileEx_function_00A1DEA0.md) (function, `0x00A1DEA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1DE40  48 83 EC 58                     sub rsp, 0x58
00A1DE44  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1DE4B  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
00A1DE53  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00A1DE57  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
00A1DE5E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A1DE62  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
00A1DE69  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A1DE6D  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00A1DE75  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1DE7A  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00A1DE82  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1DE87  E8 14 00 00 00                  call 0x140a1dea0
00A1DE8C  48 83 C4 58                     add rsp, 0x58
00A1DE90  C3                              ret
00A1DE91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtNotifyChangeDirectoryFile(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned __int8 a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int8 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m10 = 1;
    v_stack_m18 = a9;
    v_stack_m20 = (unsigned int)((unsigned int)(a8));
    v_stack_m28 = (unsigned int)((unsigned int)(a7));
    v_stack_m30 = a6;
    v_stack_m38 = a5;
    result = NtNotifyChangeDirectoryFileEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtNotifyChangeDirectoryFile(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, uint8_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint8_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m10 = 1;
    v_stack_m18 = Arg9;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m30 = Arg6;
    v_stack_m38 = Arg5;
    result = NtNotifyChangeDirectoryFileEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1DE40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A1DE40[BB_00A1DE40]
  bb_00A1DE91[BB_00A1DE91]
```
