# VslConfigureSecureAtsDevice

- RVA: `0x0058E044`–`0x0058E0C8` (길이 `132` bytes)
- VA: `0x000000014058E044`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3900`
- 디코드: `31`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058E074` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0058E0A1` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x0058E0B1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpAtsConfigureSecureDevice](../65/ExpAtsConfigureSecureDevice_function_00659E3C.md) at `0x00659EB3`

### Static image references
- `0x0058E051` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058E044  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0058E049  57                              push rdi
0058E04A  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058E051  48 8B 05 E8 C6 87 00            mov rax, qword ptr [rip + 0x87c6e8]
0058E058  48 33 C4                        xor rax, rsp
0058E05B  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0058E063  48 8B FA                        mov rdi, rdx
0058E066  48 8B D9                        mov rbx, rcx
0058E069  33 D2                           xor edx, edx
0058E06B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058E070  44 8D 42 68                     lea r8d, [rdx + 0x68]
0058E074  E8 C7 8B 13 00                  call 0x1406c6c40
0058E079  8B 43 08                        mov eax, dword ptr [rbx + 8]
0058E07C  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0058E081  F2 0F 10 03                     movsd xmm0, qword ptr [rbx]
0058E085  BA 15 01 00 00                  mov edx, 0x115
0058E08A  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0058E08E  45 33 C0                        xor r8d, r8d
0058E091  48 8B 07                        mov rax, qword ptr [rdi]
0058E094  B1 02                           mov cl, 2
0058E096  48 89 44 24 34                  mov qword ptr [rsp + 0x34], rax
0058E09B  F2 0F 11 44 24 28               movsd qword ptr [rsp + 0x28], xmm0
0058E0A1  E8 AA 7D CA FF                  call 0x140235e50
0058E0A6  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0058E0AE  48 33 CC                        xor rcx, rsp
0058E0B1  E8 8A E5 11 00                  call 0x1406ac640
0058E0B6  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0058E0BE  48 81 C4 A0 00 00 00            add rsp, 0xa0
0058E0C5  5F                              pop rdi
0058E0C6  C3                              ret
0058E0C7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslConfigureSecureAtsDevice(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8898280)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    a3 = 0;
    v_stack_m74 = *(unsigned __int64 *)(a2);
    v_stack_m80 = v_xmm0;
    result = VslpEnterIumSecureMode(2, 277, a3, v_stack_m88);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 277, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslConfigureSecureAtsDevice(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87C6E8)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)));
    a3 = 0;
    v_stack_m74 = *(uint64_t *)(arg2);
    v_stack_m80 = v_xmm0;
    result = VslpEnterIumSecureMode(2, 277, a3, v_stack_m88);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 277, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058E044&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058E044[BB_0058E044]
  bb_0058E0C7[BB_0058E0C7]
```
