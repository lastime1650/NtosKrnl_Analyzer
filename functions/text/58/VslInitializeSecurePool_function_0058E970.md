# VslInitializeSecurePool

- RVA: `0x0058E970`–`0x0058E9F7` (길이 `135` bytes)
- VA: `0x000000014058E970`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B53F0`
- 디코드: `30`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0058E9A0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0058E9D0` → [VslpEnterIumSecureMode](../23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x0058E9E0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5EB43`

### Static image references
- `0x0058E97D` → RVA `0x00E0A740` (`.data`; read)
- `0x0058E9A9` → RVA `0x00EFA900` (`.data`; write)
- `0x0058E9B5` → RVA `0x00EFA908` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058E970  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0058E975  57                              push rdi
0058E976  48 81 EC A0 00 00 00            sub rsp, 0xa0
0058E97D  48 8B 05 BC BD 87 00            mov rax, qword ptr [rip + 0x87bdbc]
0058E984  48 33 C4                        xor rax, rsp
0058E987  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0058E98F  48 8B FA                        mov rdi, rdx
0058E992  48 8B D9                        mov rbx, rcx
0058E995  33 D2                           xor edx, edx
0058E997  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0058E99C  44 8D 42 68                     lea r8d, [rdx + 0x68]
0058E9A0  E8 9B 82 13 00                  call 0x1406c6c40
0058E9A5  48 8D 04 3B                     lea rax, [rbx + rdi]
0058E9A9  48 89 1D 50 BF 96 00            mov qword ptr [rip + 0x96bf50], rbx
0058E9B0  BA D6 00 00 00                  mov edx, 0xd6
0058E9B5  48 89 05 4C BF 96 00            mov qword ptr [rip + 0x96bf4c], rax
0058E9BC  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
0058E9C1  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0058E9C6  45 33 C0                        xor r8d, r8d
0058E9C9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0058E9CE  B1 02                           mov cl, 2
0058E9D0  E8 7B 74 CA FF                  call 0x140235e50
0058E9D5  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
0058E9DD  48 33 CC                        xor rcx, rsp
0058E9E0  E8 5B DC 11 00                  call 0x1406ac640
0058E9E5  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
0058E9ED  48 81 C4 A0 00 00 00            add rsp, 0xa0
0058E9F4  5F                              pop rdi
0058E9F5  C3                              ret
0058E9F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslInitializeSecurePool(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8895932)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    *(unsigned __int64 *)(v_rip + 9879376) = a1;
    *(unsigned __int64 *)(v_rip + 9879372) = a1 + a2 * 1;
    v_stack_m80 = a1;
    a3 = 0;
    v_stack_m78 = 0;
    result = VslpEnterIumSecureMode(2, 214, a3, v_stack_m88);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 214, a3, v_stack_m88);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslInitializeSecurePool(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x87BDBC)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    *(void **)(v_rip + 0x96BF50) = Arg1;
    *(void **)(v_rip + 0x96BF4C) = Arg1 + Arg2 * 1;
    v_stack_m80 = Arg1;
    a3 = 0;
    v_stack_m78 = 0;
    result = VslpEnterIumSecureMode(2, 214, a3, v_stack_m88);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 214, a3, v_stack_m88);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdi*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058E970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058E970[BB_0058E970]
  bb_0058E9F6[BB_0058E9F6]
```
