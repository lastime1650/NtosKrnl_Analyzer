# VslResetKernelShadowStack

- RVA: `0x00A6577C`–`0x00A657FE` (길이 `130` bytes)
- VA: `0x0000000140A6577C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3900`
- 디코드: `32`개 명령, `130/130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A657AB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A657CB` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x00A657E7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MmDeleteKernelStack](../../text/33/MmDeleteKernelStack_function_0033A960.md) at `0x0033AF3C`

### Static image references
- `0x00A65789` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A657AB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A657CB` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (`PAGE` → `.text`)
  - `0x00A657E7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6577C  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A65781  57                              push rdi
00A65782  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A65789  48 8B 05 B0 4F 3A 00            mov rax, qword ptr [rip + 0x3a4fb0]
00A65790  48 33 C4                        xor rax, rsp
00A65793  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A6579B  48 8B FA                        mov rdi, rdx
00A6579E  8B D9                           mov ebx, ecx
00A657A0  33 D2                           xor edx, edx
00A657A2  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A657A7  44 8D 42 68                     lea r8d, [rdx + 0x68]
00A657AB  E8 90 14 C6 FF                  call 0x1406c6c40
00A657B0  48 8B 07                        mov rax, qword ptr [rdi]
00A657B3  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00A657B8  BA E8 00 00 00                  mov edx, 0xe8
00A657BD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A657C2  45 33 C0                        xor r8d, r8d
00A657C5  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A657C9  B1 02                           mov cl, 2
00A657CB  E8 80 06 7D FF                  call 0x140235e50
00A657D0  85 C0                           test eax, eax
00A657D2  78 08                           js 0x140a657dc
00A657D4  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00A657D9  48 89 0F                        mov qword ptr [rdi], rcx
00A657DC  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A657E4  48 33 CC                        xor rcx, rsp
00A657E7  E8 54 6E C4 FF                  call 0x1406ac640
00A657EC  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00A657F4  48 81 C4 A0 00 00 00            add rsp, 0xa0
00A657FB  5F                              pop rdi
00A657FC  C3                              ret
00A657FD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslResetKernelShadowStack(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3821488)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m78 = *(unsigned __int64 *)(a2);
    a3 = 0;
    v_stack_m80 = (unsigned int)((unsigned int)(a1));
    result = VslpEnterIumSecureMode(2, 232, a3, v_stack_m88);
    if (!(sign_flag)) {
        a1 = v_stack_m78;
        *(unsigned __int64 *)(a2) = a1;
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 232, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslResetKernelShadowStack(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x3A4FB0)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m78 = *(uint64_t *)(arg2);
    a3 = 0;
    v_stack_m80 = (uint32_t)((uint32_t)(Arg1));
    result = VslpEnterIumSecureMode(2, 232, a3, v_stack_m88);
    if (!(sign_flag)) {
        Arg1 = v_stack_m78;
        *(uint64_t *)(arg2) = Arg1;
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 232, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6577C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6577C[BB_00A6577C]
  bb_00A657D4[BB_00A657D4]
  bb_00A657DC[BB_00A657DC]
  bb_00A657FD[BB_00A657FD]
  bb_00A6577C -->|branch| bb_00A657DC
  bb_00A6577C -->|fallthrough| bb_00A657D4
  bb_00A657D4 -->|flow| bb_00A657DC
```
