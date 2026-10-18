# ViZwCheckObjectAttributes

- RVA: `0x00BA4C80`–`0x00BA4CCA` (길이 `74` bytes)
- VA: `0x0000000140BA4C80`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084918`
- 디코드: `22`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **22**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA4C95` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4CA1` → [ViZwCheckUnicodeString](ViZwCheckUnicodeString_function_00BA4CD0.md) (function, `0x00BA4CD0`)
- `0x00BA4CAD` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)
- `0x00BA4CB9` → [ViZwCheckVirtualAddress](ViZwCheckVirtualAddress_function_00BA4D68.md) (function, `0x00BA4D68`)

### Direct callers
- [VfZwAlpcAcceptConnectPort_Entry](VfZwAlpcAcceptConnectPort_Entry_function_00BA3D90.md) at `0x00BA3DD9`
- [VfZwAlpcConnectPort_Entry](VfZwAlpcConnectPort_Entry_function_00BA3DF0.md) at `0x00BA3E69`
- [VfZwAlpcCreatePort_Entry](VfZwAlpcCreatePort_Entry_function_00BA3E90.md) at `0x00BA3EC1`
- [VfZwCreateDirectoryObject_Entry](VfZwCreateDirectoryObject_Entry_function_00BA40A0.md) at `0x00BA40C5`
- [VfZwCreateEnlistment_Entry](VfZwCreateEnlistment_Entry_function_00BA40E0.md) at `0x00BA4105`
- [VfZwCreateEvent_Entry](VfZwCreateEvent_Entry_function_00BA4120.md) at `0x00BA4145`
- [VfZwCreateFile_Entry](VfZwCreateFile_Entry_function_00BA4160.md) at `0x00BA4185`
- [VfZwCreateKey_Entry](VfZwCreateKey_Entry_function_00BA41C0.md) at `0x00BA41E5`
- [VfZwCreateSection_Entry](VfZwCreateSection_Entry_function_00BA4210.md) at `0x00BA4235`
- [VfZwCreateSymbolicLinkObject_Entry](VfZwCreateSymbolicLinkObject_Entry_function_00BA4260.md) at `0x00BA4285`
- [VfZwCreateTransactionManager_Entry](VfZwCreateTransactionManager_Entry_function_00BA42B0.md) at `0x00BA42D5`
- [VfZwCreateTransaction_Entry](VfZwCreateTransaction_Entry_function_00BA4300.md) at `0x00BA433D`
- [VfZwDeleteFile_Entry](VfZwDeleteFile_Entry_function_00BA4390.md) at `0x00BA43A7`
- [VfZwDuplicateToken_Entry](VfZwDuplicateToken_Entry_function_00BA4490.md) at `0x00BA44A9`
- [VfZwLoadKey_Entry](VfZwLoadKey_Entry_function_00BA4560.md) at `0x00BA4579`
- [VfZwLoadKey_Entry](VfZwLoadKey_Entry_function_00BA4560.md) at `0x00BA4585`
- [VfZwOpenEnlistment_Entry](VfZwOpenEnlistment_Entry_function_00BA4670.md) at `0x00BA4695`
- [VfZwOpenFile_Entry](VfZwOpenFile_Entry_function_00BA46B0.md) at `0x00BA46D5`
- [VfZwOpenProcess_Entry](VfZwOpenProcess_Entry_function_00BA4700.md) at `0x00BA4725`
- [VfZwOpenTransactionManager_Entry](VfZwOpenTransactionManager_Entry_function_00BA4750.md) at `0x00BA4775`
- [VfZwOpenTransaction_Entry](VfZwOpenTransaction_Entry_function_00BA47A0.md) at `0x00BA47D1`
- [VfZwQueryFullAttributesFile_Entry](VfZwQueryFullAttributesFile_Entry_function_00BA4970.md) at `0x00BA4989`
- [VfZwReplaceKey_Entry](VfZwReplaceKey_Entry_function_00BA4B50.md) at `0x00BA4B69`
- [VfZwReplaceKey_Entry](VfZwReplaceKey_Entry_function_00BA4B50.md) at `0x00BA4B75`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA4C80  48 85 C9                        test rcx, rcx
00BA4C83  74 43                           je 0x140ba4cc8
00BA4C85  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BA4C8A  57                              push rdi
00BA4C8B  48 83 EC 20                     sub rsp, 0x20
00BA4C8F  48 8B FA                        mov rdi, rdx
00BA4C92  48 8B D9                        mov rbx, rcx
00BA4C95  E8 CE 00 00 00                  call 0x140ba4d68
00BA4C9A  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00BA4C9E  48 8B D7                        mov rdx, rdi
00BA4CA1  E8 2A 00 00 00                  call 0x140ba4cd0
00BA4CA6  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00BA4CAA  48 8B D7                        mov rdx, rdi
00BA4CAD  E8 B6 00 00 00                  call 0x140ba4d68
00BA4CB2  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
00BA4CB6  48 8B D7                        mov rdx, rdi
00BA4CB9  E8 AA 00 00 00                  call 0x140ba4d68
00BA4CBE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BA4CC3  48 83 C4 20                     add rsp, 0x20
00BA4CC7  5F                              pop rdi
00BA4CC8  C3                              ret
00BA4CC9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViZwCheckObjectAttributes(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    if (a1 != 0) {
        v_stack_p8 = v_rbx;
        v_rsp = (v_rsp) - (32);
        v_rdi = a2;
        v_rbx = a1;
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbx + 16);
        a2 = v_rdi;
        result = ViZwCheckUnicodeString(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbx + 32);
        a2 = v_rdi;
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbx + 40);
        a2 = v_rdi;
        result = ViZwCheckVirtualAddress(a1, a2, a3, a4);
        v_rbx = v_stack_p8;
        v_rsp = (v_rsp) + (32);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViZwCheckObjectAttributes(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    if (Arg1 != 0) {
        v_stack_p8 = local_rbx;
        local_rsp = (local_rsp) - (32);
        local_rdi = Arg2;
        local_rbx = Arg1;
        result = ViZwCheckVirtualAddress(Arg1, Arg2, a3, a4);
        Arg1 = *(uint64_t *)(local_rbx + 0x10);
        Arg2 = local_rdi;
        result = ViZwCheckUnicodeString(Arg1, Arg2, a3, a4);
        Arg1 = *(uint64_t *)(local_rbx + 0x20);
        Arg2 = local_rdi;
        result = ViZwCheckVirtualAddress(Arg1, Arg2, a3, a4);
        Arg1 = *(uint64_t *)(local_rbx + 0x28);
        Arg2 = local_rdi;
        result = ViZwCheckVirtualAddress(Arg1, Arg2, a3, a4);
        local_rbx = v_stack_p8;
        local_rsp = (local_rsp) + (32);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA4C80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA4C80[BB_00BA4C80]
  bb_00BA4C85[BB_00BA4C85]
  bb_00BA4CC8[BB_00BA4CC8]
  bb_00BA4CC9[BB_00BA4CC9]
  bb_00BA4C80 -->|branch| bb_00BA4CC8
  bb_00BA4C80 -->|fallthrough| bb_00BA4C85
  bb_00BA4C85 -->|flow| bb_00BA4CC8
```
