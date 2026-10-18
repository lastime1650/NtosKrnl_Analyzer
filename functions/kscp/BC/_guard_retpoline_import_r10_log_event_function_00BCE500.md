# _guard_retpoline_import_r10_log_event

- RVA: `0x00BCE500`–`0x00BCE557` (길이 `87` bytes)
- VA: `0x0000000140BCE500`
- 실행 섹션: `KSCP`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2120`
- 디코드: `19`개 명령, `87/87` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BCE532` → `indirect target` (indirect, 간접 대상)

### Direct callers
- [_guard_retpoline_import_r10](_guard_retpoline_import_r10_function_00BCE420.md) at `0x00BCE48A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BCE500  48 83 EC 58                     sub rsp, 0x58
00BCE504  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00BCE509  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00BCE50E  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00BCE513  4C 89 44 24 38                  mov qword ptr [rsp + 0x38], r8
00BCE518  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00BCE51D  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
00BCE522  0F AE E8                        lfence
00BCE525  49 8B CA                        mov rcx, r10
00BCE528  48 B8 00 00 65 40 01 00 00 00   movabs rax, 0x140650000
00BCE532  FF D0                           call rax
00BCE534  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
00BCE539  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
00BCE53E  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00BCE543  4C 8B 44 24 38                  mov r8, qword ptr [rsp + 0x38]
00BCE548  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00BCE54D  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
00BCE552  48 83 C4 58                     add rsp, 0x58
00BCE556  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall _guard_retpoline_import_r10_log_event(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m38 = result;
    v_stack_m30 = a1;
    v_stack_m28 = a2;
    v_stack_m20 = a3;
    v_stack_m18 = a4;
    v_stack_m10 = v_r10;
    result = kernel_indirect_call(v_r10, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t _guard_retpoline_import_r10_log_event(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m38 = result;
    v_stack_m30 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m20 = Arg3;
    v_stack_m18 = Arg4;
    v_stack_m10 = local_r10;
    result = kernel_indirect_call(local_r10, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kscp&rva=0x00BCE500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BCE500[BB_00BCE500]
```
