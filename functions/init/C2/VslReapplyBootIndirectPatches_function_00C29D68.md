# VslReapplyBootIndirectPatches

- RVA: `0x00C29D68`–`0x00C29DE7` (길이 `127` bytes)
- VA: `0x0000000140C29D68`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF554`
- 디코드: `29`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C29D91` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C29DB1` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x00C29DD8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmReapplyBootPatchImports](../C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C6788F`
- [MiInitializeLoadedModuleList](../C6/MiInitializeLoadedModuleList_function_00C6BCDC.md) at `0x00C6BF47`

### Static image references
- `0x00C29D71` → RVA `0x00E0A740` (`.data`; read)
- `0x00C29D96` → RVA `0x00F8EC2C` (`.data`; read/write)
- `0x00C29DB8` → RVA `0x00F8EC34` (`.data`; read)
- `0x00C29DBF` → RVA `0x00F8EC30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00C29D91` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C29DB1` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (`INIT` → `.text`)
  - `0x00C29DD8` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C29D68  40 53                           push rbx
00C29D6A  48 81 EC A0 00 00 00            sub rsp, 0xa0
00C29D71  48 8B 05 C8 09 1E 00            mov rax, qword ptr [rip + 0x1e09c8]
00C29D78  48 33 C4                        xor rax, rsp
00C29D7B  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00C29D83  33 D2                           xor edx, edx
00C29D85  48 8B D9                        mov rbx, rcx
00C29D88  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00C29D8D  44 8D 42 68                     lea r8d, [rdx + 0x68]
00C29D91  E8 AA CE A9 FF                  call 0x1406c6c40
00C29D96  F0 FF 05 8F 4E 36 00            lock inc dword ptr [rip + 0x364e8f]
00C29D9D  BA DE 00 00 00                  mov edx, 0xde
00C29DA2  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00C29DA7  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00C29DAC  45 33 C0                        xor r8d, r8d
00C29DAF  B1 02                           mov cl, 2
00C29DB1  E8 9A C0 60 FF                  call 0x140235e50
00C29DB6  85 C0                           test eax, eax
00C29DB8  48 8D 15 75 4E 36 00            lea rdx, [rip + 0x364e75]
00C29DBF  48 8D 0D 6A 4E 36 00            lea rcx, [rip + 0x364e6a]
00C29DC6  48 0F 48 CA                     cmovs rcx, rdx
00C29DCA  F0 FF 01                        lock inc dword ptr [rcx]
00C29DCD  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00C29DD5  48 33 CC                        xor rcx, rsp
00C29DD8  E8 63 28 A8 FF                  call 0x1406ac640
00C29DDD  48 81 C4 A0 00 00 00            add rsp, 0xa0
00C29DE4  5B                              pop rbx
00C29DE5  C3                              ret
00C29DE6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslReapplyBootIndirectPatches(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 1968584)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = a1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 222, a3, v_stack_m88);
    a1 = v_rip + 3559018;
    if (sign_flag) { a1 = v_rip + 3559029; }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip + 3559029, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslReapplyBootIndirectPatches(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x1E09C8)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = Arg1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 222, a3, v_stack_m88);
    Arg1 = v_rip + 3559018;
    if (sign_flag) { Arg1 = v_rip + 3559029; }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip + 3559029, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C29D68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C29D68[BB_00C29D68]
  bb_00C29DE6[BB_00C29DE6]
```
