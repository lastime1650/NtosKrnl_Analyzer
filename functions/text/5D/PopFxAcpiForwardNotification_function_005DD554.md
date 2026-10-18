# PopFxAcpiForwardNotification

- RVA: `0x005DD554`–`0x005DD5ED` (길이 `153` bytes)
- VA: `0x00000001405DD554`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `40`개 명령, `153/153` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005DD599` → [IoAcquireRemoveLockEx](../43/IoAcquireRemoveLockEx_function_00433420.md) (function, `0x00433420`)
- `0x005DD5AE` → [PopPluginAcpiNotification](../4D/PopPluginAcpiNotification_function_004D9820.md) (function, `0x004D9820`)
- `0x005DD5C3` → [IoReleaseRemoveLockEx](../33/IoReleaseRemoveLockEx_function_0033D330.md) (function, `0x0033D330`)

### Direct callers
- [PopFxAcpiDispatchNotification](PopFxAcpiDispatchNotification_function_005DD450.md) at `0x005DD4B5`

### Static image references
- `0x005DD584` → RVA `0x006C7800` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD554  48 8B C4                        mov rax, rsp
005DD557  48 89 58 08                     mov qword ptr [rax + 8], rbx
005DD55B  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
005DD55F  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
005DD563  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
005DD567  41 56                           push r14
005DD569  48 83 EC 30                     sub rsp, 0x30
005DD56D  48 8D B1 38 01 00 00            lea rsi, [rcx + 0x138]
005DD574  C7 40 E8 20 00 00 00            mov dword ptr [rax - 0x18], 0x20
005DD57B  49 8B E8                        mov rbp, r8
005DD57E  44 8B F2                        mov r14d, edx
005DD581  48 8B D9                        mov rbx, rcx
005DD584  4C 8D 05 75 A2 0E 00            lea r8, [rip + 0xea275]
005DD58B  48 8B CE                        mov rcx, rsi
005DD58E  41 B9 01 00 00 00               mov r9d, 1
005DD594  BA 50 6F 46 72                  mov edx, 0x72466f50
005DD599  E8 82 5E E5 FF                  call 0x140433420
005DD59E  8B F8                           mov edi, eax
005DD5A0  85 C0                           test eax, eax
005DD5A2  78 2B                           js 0x1405dd5cf
005DD5A4  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
005DD5A8  4C 8B C5                        mov r8, rbp
005DD5AB  41 8B D6                        mov edx, r14d
005DD5AE  E8 6D C2 EF FF                  call 0x1404d9820
005DD5B3  BA 50 6F 46 72                  mov edx, 0x72466f50
005DD5B8  41 B8 20 00 00 00               mov r8d, 0x20
005DD5BE  48 8B CE                        mov rcx, rsi
005DD5C1  8A D8                           mov bl, al
005DD5C3  E8 68 FD D5 FF                  call 0x14033d330
005DD5C8  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
005DD5CD  88 19                           mov byte ptr [rcx], bl
005DD5CF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005DD5D4  8B C7                           mov eax, edi
005DD5D6  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
005DD5DB  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
005DD5E0  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
005DD5E5  48 83 C4 30                     add rsp, 0x30
005DD5E9  41 5E                           pop r14
005DD5EB  C3                              ret
005DD5EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxAcpiForwardNotification(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned int *)(v_rsp - 24) = 32;
    result = IoAcquireRemoveLockEx(a1 + 312, (unsigned int)(0x72466F50ULL), v_rip + 959093, 1);
    v_rbx = a1;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1 + 80);
        a3 = a3;
        a2 = (unsigned int)((unsigned int)(a2));
        result = PopPluginAcpiNotification(a1, a2, a3, 1);
        a2 = 0x72466F50ULL;
        a3 = 32;
        a1 = a1 + 312;
        v_rbx = (unsigned __int8)(result);
        result = IoReleaseRemoveLockEx(a1, a2, a3, 1);
        a1 = a5;
        *(unsigned __int8 *)(a1) = (unsigned __int8)(v_rbx);
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PopFxAcpiForwardNotification(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint32_t *)(local_rsp - 0x18) = 32;
    result = IoAcquireRemoveLockEx(Arg1 + 312, (uint32_t)(0x72466F50ULL), v_rip + 959093, 1);
    local_rbx = Arg1;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1 + 0x50);
        Arg3 = Arg3;
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        result = PopPluginAcpiNotification(Arg1, Arg2, Arg3, 1);
        Arg2 = 0x72466F50ULL;
        Arg3 = 32;
        Arg1 = Arg1 + 312;
        local_rbx = (uint8_t)(result);
        result = IoReleaseRemoveLockEx(Arg1, Arg2, Arg3, 1);
        Arg1 = Arg5;
        *(uint8_t *)(arg1) = (uint8_t)(local_rbx);
    }
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x138` | `64` | `R` |
| `Arg5` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD554&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD554[BB_005DD554]
  bb_005DD5A4[BB_005DD5A4]
  bb_005DD5CF[BB_005DD5CF]
  bb_005DD5EC[BB_005DD5EC]
  bb_005DD554 -->|branch| bb_005DD5CF
  bb_005DD554 -->|fallthrough| bb_005DD5A4
  bb_005DD5A4 -->|flow| bb_005DD5CF
```
