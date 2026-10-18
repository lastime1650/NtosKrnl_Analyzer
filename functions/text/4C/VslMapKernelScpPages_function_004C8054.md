# VslMapKernelScpPages

- RVA: `0x004C8054`–`0x004C80B5` (길이 `97` bytes)
- VA: `0x00000001404C8054`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF554`
- 디코드: `23`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004C807D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C8096` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x004C80A6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiMapKernelScp](../4D/MiMapKernelScp_function_004DCAD4.md) at `0x004DCB22`

### Static image references
- `0x004C805D` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C8054  40 53                           push rbx
004C8056  48 81 EC A0 00 00 00            sub rsp, 0xa0
004C805D  48 8B 05 DC 26 94 00            mov rax, qword ptr [rip + 0x9426dc]
004C8064  48 33 C4                        xor rax, rsp
004C8067  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
004C806F  33 D2                           xor edx, edx
004C8071  48 8B D9                        mov rbx, rcx
004C8074  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
004C8079  44 8D 42 68                     lea r8d, [rdx + 0x68]
004C807D  E8 BE EB 1F 00                  call 0x1406c6c40
004C8082  BA DB 00 00 00                  mov edx, 0xdb
004C8087  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
004C808C  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
004C8091  45 33 C0                        xor r8d, r8d
004C8094  B1 02                           mov cl, 2
004C8096  E8 B5 DD D6 FF                  call 0x140235e50
004C809B  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004C80A3  48 33 CC                        xor rcx, rsp
004C80A6  E8 95 45 1E 00                  call 0x1406ac640
004C80AB  48 81 C4 A0 00 00 00            add rsp, 0xa0
004C80B2  5B                              pop rbx
004C80B3  C3                              ret
004C80B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslMapKernelScpPages(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 9709276)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = a1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 219, a3, v_stack_m88);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 219, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslMapKernelScpPages(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x9426DC)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = Arg1;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 219, a3, v_stack_m88);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 219, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C8054&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C8054[BB_004C8054]
  bb_004C80B4[BB_004C80B4]
```
