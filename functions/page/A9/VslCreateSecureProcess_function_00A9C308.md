# VslCreateSecureProcess

- RVA: `0x00A9C308`–`0x00A9C395` (길이 `141` bytes)
- VA: `0x0000000140A9C308`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AFF04`
- 디코드: `35`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A9C340` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A9C35E` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x00A9C37A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeInitializeProcess](../A6/KeInitializeProcess_function_00A63CF4.md) at `0x00A64150`
- [VslCreateEnclave](VslCreateEnclave_function_00A9C18C.md) at `0x00A9C2A6`

### Static image references
- `0x00A9C31A` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A9C340` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A9C35E` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (`PAGE` → `.text`)
  - `0x00A9C37A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9C308  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A9C30D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A9C312  57                              push rdi
00A9C313  48 81 EC A0 00 00 00            sub rsp, 0xa0
00A9C31A  48 8B 05 1F E4 36 00            mov rax, qword ptr [rip + 0x36e41f]
00A9C321  48 33 C4                        xor rax, rsp
00A9C324  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A9C32C  48 8B FA                        mov rdi, rdx
00A9C32F  49 8B F0                        mov rsi, r8
00A9C332  33 D2                           xor edx, edx
00A9C334  48 8B D9                        mov rbx, rcx
00A9C337  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A9C33C  44 8D 42 68                     lea r8d, [rdx + 0x68]
00A9C340  E8 FB A8 C2 FF                  call 0x1406c6c40
00A9C345  BA 06 00 00 00                  mov edx, 6
00A9C34A  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
00A9C34F  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00A9C354  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00A9C359  45 33 C0                        xor r8d, r8d
00A9C35C  B1 02                           mov cl, 2
00A9C35E  E8 ED 9A 79 FF                  call 0x140235e50
00A9C363  85 C0                           test eax, eax
00A9C365  78 08                           js 0x140a9c36f
00A9C367  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00A9C36C  48 89 0E                        mov qword ptr [rsi], rcx
00A9C36F  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00A9C377  48 33 CC                        xor rcx, rsp
00A9C37A  E8 C1 02 C1 FF                  call 0x1406ac640
00A9C37F  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
00A9C387  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00A9C38B  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00A9C38F  49 8B E3                        mov rsp, r11
00A9C392  5F                              pop rdi
00A9C393  C3                              ret
00A9C394  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VslCreateSecureProcess(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3597343)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_m88, a2, a2 + 104, a4);
    v_stack_m80 = a1;
    v_stack_m78 = 0;
    a3 = 0;
    result = VslpEnterIumSecureMode(2, 6, a3, v_stack_m88);
    if (!(sign_flag)) {
        a1 = v_stack_m78;
        *(unsigned __int64 *)(a3) = a1;
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 6, a3, v_stack_m88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VslCreateSecureProcess(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x36E41F)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_m88, Arg2, Arg2 + 104, a4);
    v_stack_m80 = Arg1;
    v_stack_m78 = 0;
    Arg3 = 0;
    result = VslpEnterIumSecureMode(2, 6, Arg3, v_stack_m88);
    if (!(sign_flag)) {
        Arg1 = v_stack_m78;
        *(uint64_t *)(arg3) = Arg1;
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 6, Arg3, v_stack_m88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9C308&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9C308[BB_00A9C308]
  bb_00A9C367[BB_00A9C367]
  bb_00A9C36F[BB_00A9C36F]
  bb_00A9C394[BB_00A9C394]
  bb_00A9C308 -->|branch| bb_00A9C36F
  bb_00A9C308 -->|fallthrough| bb_00A9C367
  bb_00A9C367 -->|flow| bb_00A9C36F
```
