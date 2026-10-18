# CmpFullPromoteHiveRootFromKcbStack

- RVA: `0x007F3F90`–`0x007F4068` (길이 `216` bytes)
- VA: `0x00000001407F3F90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D73B8`
- 디코드: `57`개 명령, `216/216` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007F3FCA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007F3FD4` → [CmpInitializeKeyNodeStack](../94/CmpInitializeKeyNodeStack_function_00946804.md) (function, `0x00946804`)
- `0x007F3FE0` → [CmpGetKcbAtLayerHeight](../94/CmpGetKcbAtLayerHeight_function_00949210.md) (function, `0x00949210`)
- `0x007F3FF3` → [CmpStartKeyNodeStackFromKcbStack](../94/CmpStartKeyNodeStackFromKcbStack_function_00945254.md) (function, `0x00945254`)
- `0x007F4005` → [CmpFullPromoteSingleKeyFromKeyNodeStacks](../8B/CmpFullPromoteSingleKeyFromKeyNodeStacks_function_008B1A40.md) (function, `0x008B1A40`)
- `0x007F4019` → [CmpKeyNodeStackGetEntryAtLayerHeight](../94/CmpKeyNodeStackGetEntryAtLayerHeight_function_00946ABC.md) (function, `0x00946ABC`)
- `0x007F4032` → [CmpRebuildKcbCacheFromNode](../84/CmpRebuildKcbCacheFromNode_function_0084C5A8.md) (function, `0x0084C5A8`)
- `0x007F403E` → [CmpCleanupKeyNodeStack](../94/CmpCleanupKeyNodeStack_function_00946A5C.md) (function, `0x00946A5C`)
- `0x007F404D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpPromoteKey](../84/CmpPromoteKey_function_00844388.md) at `0x0084455A`

### Static image references
- `0x007F3FA2` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007F3FCA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007F404D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F3F90  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
007F3F95  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
007F3F9A  57                              push rdi
007F3F9B  48 81 EC 80 00 00 00            sub rsp, 0x80
007F3FA2  48 8B 05 97 67 61 00            mov rax, qword ptr [rip + 0x616797]
007F3FA9  48 33 C4                        xor rax, rsp
007F3FAC  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007F3FB1  33 C0                           xor eax, eax
007F3FB3  48 8B F1                        mov rsi, rcx
007F3FB6  33 D2                           xor edx, edx
007F3FB8  89 44 24 22                     mov dword ptr [rsp + 0x22], eax
007F3FBC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007F3FC1  66 89 44 24 26                  mov word ptr [rsp + 0x26], ax
007F3FC6  44 8D 40 4A                     lea r8d, [rax + 0x4a]
007F3FCA  E8 71 2C ED FF                  call 0x1406c6c40
007F3FCF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007F3FD4  E8 2B 28 15 00                  call 0x140946804
007F3FD9  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
007F3FDD  48 8B CE                        mov rcx, rsi
007F3FE0  E8 2B 52 15 00                  call 0x140949210
007F3FE5  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007F3FEA  45 33 C0                        xor r8d, r8d
007F3FED  48 8B D6                        mov rdx, rsi
007F3FF0  48 8B F8                        mov rdi, rax
007F3FF3  E8 5C 12 15 00                  call 0x140945254
007F3FF8  8B D8                           mov ebx, eax
007F3FFA  85 C0                           test eax, eax
007F3FFC  78 3B                           js 0x1407f4039
007F3FFE  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
007F4003  33 C9                           xor ecx, ecx
007F4005  E8 36 DA 0B 00                  call 0x1408b1a40
007F400A  8B D8                           mov ebx, eax
007F400C  85 C0                           test eax, eax
007F400E  78 29                           js 0x1407f4039
007F4010  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
007F4014  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007F4019  E8 9E 2A 15 00                  call 0x140946abc
007F401E  48 FF 87 30 01 00 00            inc qword ptr [rdi + 0x130]
007F4025  45 33 C9                        xor r9d, r9d
007F4028  45 33 C0                        xor r8d, r8d
007F402B  48 8B CF                        mov rcx, rdi
007F402E  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
007F4032  E8 71 85 05 00                  call 0x14084c5a8
007F4037  33 DB                           xor ebx, ebx
007F4039  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
007F403E  E8 19 2A 15 00                  call 0x140946a5c
007F4043  8B C3                           mov eax, ebx
007F4045  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
007F404A  48 33 CC                        xor rcx, rsp
007F404D  E8 EE 85 EB FF                  call 0x1406ac640
007F4052  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
007F405A  49 8B 5B 18                     mov rbx, qword ptr [r11 + 0x18]
007F405E  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
007F4062  49 8B E3                        mov rsp, r11
007F4065  5F                              pop rdi
007F4066  C3                              ret
007F4067  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFullPromoteHiveRootFromKcbStack(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int16 v_stack_m62;
    unsigned int v_stack_m66;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 6383511)) ^ (v_rsp);
    v_stack_m18 = result;
    result = 0;
    a2 = 0;
    v_stack_m66 = 0;
    v_stack_m62 = 0;
    result = memset(v_stack_m68, a2, result + 74, a4);
    result = CmpInitializeKeyNodeStack(v_stack_m68, a2, result + 74, a4);
    result = CmpGetKcbAtLayerHeight(a1, *(unsigned __int16 *)(a1 + 2), result + 74, a4);
    a3 = 0;
    result = CmpStartKeyNodeStackFromKcbStack(v_stack_m68, a1, a3, a4);
    if (sign_flag) goto loc_007F4039;
    a1 = 0;
    result = CmpFullPromoteSingleKeyFromKeyNodeStacks(a1, v_stack_m68, a3, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = *(unsigned __int16 *)(a1 + 2);
        a1 = v_stack_m68;
        result = CmpKeyNodeStackGetEntryAtLayerHeight(a1, a2, a3, a4);
        a4 = 0;
        a3 = 0;
        a1 = result;
        a2 = *(unsigned __int64 *)(result + 16);
        result = CmpRebuildKcbCacheFromNode(a1, a2, a3, a4);
        v_rbx = 0;
    }
    result = CmpCleanupKeyNodeStack(v_stack_m68, a2, a3, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFullPromoteHiveRootFromKcbStack(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint16_t v_stack_m62;
    uint32_t v_stack_m66;
    uint64_t v_stack_m68;
    uint64_t v_stack_m8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x616797)) ^ (local_rsp);
    v_stack_m18 = result;
    result = 0;
    Arg2 = 0;
    v_stack_m66 = 0;
    v_stack_m62 = 0;
    result = memset(v_stack_m68, Arg2, result + 74, Arg4);
    result = CmpInitializeKeyNodeStack(v_stack_m68, Arg2, result + 74, Arg4);
    result = CmpGetKcbAtLayerHeight(Arg1, *(uint16_t *)(arg1 + 0x2), result + 74, Arg4);
    Arg3 = 0;
    result = CmpStartKeyNodeStackFromKcbStack(v_stack_m68, Arg1, Arg3, Arg4);
    if (sign_flag) goto loc_007F4039;
    Arg1 = 0;
    result = CmpFullPromoteSingleKeyFromKeyNodeStacks(Arg1, v_stack_m68, Arg3, Arg4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = *(uint16_t *)(arg1 + 0x2);
        Arg1 = v_stack_m68;
        result = CmpKeyNodeStackGetEntryAtLayerHeight(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
        Arg3 = 0;
        Arg1 = result;
        Arg2 = *(uint64_t *)(result + 0x10);
        result = CmpRebuildKcbCacheFromNode(Arg1, Arg2, Arg3, Arg4);
        local_rbx = 0;
    }
    result = CmpCleanupKeyNodeStack(v_stack_m68, Arg2, Arg3, Arg4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F3F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F3F90[BB_007F3F90]
  bb_007F3FFE[BB_007F3FFE]
  bb_007F4010[BB_007F4010]
  bb_007F4039[BB_007F4039]
  bb_007F4067[BB_007F4067]
  bb_007F3F90 -->|branch| bb_007F4039
  bb_007F3F90 -->|fallthrough| bb_007F3FFE
  bb_007F3FFE -->|branch| bb_007F4039
  bb_007F3FFE -->|fallthrough| bb_007F4010
  bb_007F4010 -->|flow| bb_007F4039
```
