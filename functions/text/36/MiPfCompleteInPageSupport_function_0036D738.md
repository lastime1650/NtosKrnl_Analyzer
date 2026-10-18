# MiPfCompleteInPageSupport

- RVA: `0x0036D738`–`0x0036D830` (길이 `248` bytes)
- VA: `0x000000014036D738`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A624`
- 디코드: `55`개 명령, `248/248` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0036D76A` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0036D7AC` → [MiInitializePageFaultPacket](../22/MiInitializePageFaultPacket_function_00228EB0.md) (function, `0x00228EB0`)
- `0x0036D7C3` → [MiWaitForInPageComplete](../38/MiWaitForInPageComplete_function_00380AB8.md) (function, `0x00380AB8`)
- `0x0036D7F1` → [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) (function, `0x002B6F10`)
- `0x0036D801` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0036D823` → [MiMapWorkingSetTypeToVm](../2C/MiMapWorkingSetTypeToVm_function_002C08C4.md) (function, `0x002C08C4`)

### Direct callers
- [MiPfCompleteCoalescedIo](MiPfCompleteCoalescedIo_function_0036C344.md) at `0x0036C42A`
- [MiPfCompletePrefetchIos](MiPfCompletePrefetchIos_function_0036C4B0.md) at `0x0036C514`
- [sub_0036CA68](Unknown_function_0036CA68.md) at `0x0036CADA`
- [sub_0036CFD7](Unknown_function_0036CFD7.md) at `0x0036D00D`
- [MmWaitForCacheManagerPrefetch](MmWaitForCacheManagerPrefetch_function_0036D644.md) at `0x0036D6FB`

### Static image references
- `0x0036D745` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036D738  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0036D73D  57                              push rdi
0036D73E  48 81 EC F0 00 00 00            sub rsp, 0xf0
0036D745  48 8B 05 F4 CF A9 00            mov rax, qword ptr [rip + 0xa9cff4]
0036D74C  48 33 C4                        xor rax, rsp
0036D74F  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
0036D757  48 8B FA                        mov rdi, rdx
0036D75A  48 8B D9                        mov rbx, rcx
0036D75D  33 D2                           xor edx, edx
0036D75F  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0036D764  41 B8 98 00 00 00               mov r8d, 0x98
0036D76A  E8 D1 94 35 00                  call 0x1406c6c40
0036D76F  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0036D775  48 83 FF 01                     cmp rdi, 1
0036D779  0F 84 99 00 00 00               je 0x14036d818
0036D77F  48 8B C3                        mov rax, rbx
0036D782  45 33 C9                        xor r9d, r9d
0036D785  8B 83 C0 00 00 00               mov eax, dword ptr [rbx + 0xc0]
0036D78B  45 33 C0                        xor r8d, r8d
0036D78E  0F BA E8 19                     bts eax, 0x19
0036D792  33 D2                           xor edx, edx
0036D794  89 83 C0 00 00 00               mov dword ptr [rbx + 0xc0], eax
0036D79A  33 C9                           xor ecx, ecx
0036D79C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0036D7A1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0036D7A6  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0036D7AC  E8 FF B6 EB FF                  call 0x140228eb0
0036D7B1  48 8B D3                        mov rdx, rbx
0036D7B4  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0036D7B9  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0036D7BE  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0036D7C3  E8 F0 32 01 00                  call 0x140380ab8
0036D7C8  48 8B 93 E0 00 00 00            mov rdx, qword ptr [rbx + 0xe0]
0036D7CF  48 C1 EA 12                     shr rdx, 0x12
0036D7D3  81 E2 F8 FF FF 3F               and edx, 0x3ffffff8
0036D7D9  48 B8 00 00 00 40 FB F6 FF FF   movabs rax, 0xfffff6fb40000000
0036D7E3  48 03 D0                        add rdx, rax
0036D7E6  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
0036D7EB  45 33 C9                        xor r9d, r9d
0036D7EE  4C 8B C3                        mov r8, rbx
0036D7F1  E8 1A 97 F4 FF                  call 0x1402b6f10
0036D7F6  48 8B 8C 24 E0 00 00 00         mov rcx, qword ptr [rsp + 0xe0]
0036D7FE  48 33 CC                        xor rcx, rsp
0036D801  E8 3A EE 33 00                  call 0x1406ac640
0036D806  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
0036D80E  48 81 C4 F0 00 00 00            add rsp, 0xf0
0036D815  5F                              pop rdi
0036D816  C3                              ret
0036D817  CC                              int3
0036D818  8B 8B C0 00 00 00               mov ecx, dword ptr [rbx + 0xc0]
0036D81E  D1 E9                           shr ecx, 1
0036D820  83 E1 0F                        and ecx, 0xf
0036D823  E8 9C 30 F5 FF                  call 0x1402c08c4
0036D828  48 8B F8                        mov rdi, rax
0036D82B  E9 4F FF FF FF                  jmp 0x14036d77f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfCompleteInPageSupport(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 11128820)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    result = memset(v_stack_mB8, a2, 152, a4);
    if (0 == 1) goto loc_0036D818;
loc_0036D77F:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    *(unsigned int *)(a1 + 192) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 192)));
    a1 = 0;
    v_stack_mD0 = v_stack_mB8;
    result = MiInitializePageFaultPacket(a1, a2, a3, a4);
    v_stack_m80 = 0;
    result = MiWaitForInPageComplete(v_stack_mB8, 0, v_stack_mC8, a4);
    a2 = (*(unsigned __int64 *)(a1 + 224)) >> (18);
    a2 = (unsigned int)((a2) & (0x3FFFFFF8ULL));
    a2 = (a2) + (result);
    a4 = 0;
    result = MiFinishHardFault(v_stack_mB8, a2, 0, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 0, a4);
    v_rsp = (v_rsp) + (240);
    return result;
loc_0036D818:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 192))) >> (1));
    a1 = (unsigned int)((a1) & (15));
    result = MiMapWorkingSetTypeToVm(a1, a2, 0, a4);
    goto loc_0036D77F;
}
```

## 5. (Beta) C Style

```c
int64_t MiPfCompleteInPageSupport(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m80;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0xA9CFF4)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    result = memset(v_stack_mB8, Arg2, 152, Arg4);
    if (0 == 1) goto loc_0036D818;
loc_0036D77F:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    *(uint32_t *)(arg1 + 0xC0) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC0)));
    Arg1 = 0;
    v_stack_mD0 = v_stack_mB8;
    result = MiInitializePageFaultPacket(Arg1, Arg2, Arg3, Arg4);
    v_stack_m80 = 0;
    result = MiWaitForInPageComplete(v_stack_mB8, 0, v_stack_mC8, Arg4);
    Arg2 = (*(uint64_t *)(arg1 + 0xE0)) >> (18);
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFF8ULL));
    Arg2 = (Arg2) + (result);
    Arg4 = 0;
    result = MiFinishHardFault(v_stack_mB8, Arg2, 0, Arg4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 0, Arg4);
    local_rsp = (local_rsp) + (240);
    return result;
loc_0036D818:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0xC0))) >> (1));
    Arg1 = (uint32_t)((Arg1) & (15));
    result = MiMapWorkingSetTypeToVm(Arg1, Arg2, 0, Arg4);
    goto loc_0036D77F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `32` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `W` |
| `Arg1` | `+ 0xE0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036D738&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0036D738[BB_0036D738]
  bb_0036D77F[BB_0036D77F]
  bb_0036D817[BB_0036D817]
  bb_0036D818[BB_0036D818]
  bb_0036D738 -->|branch| bb_0036D818
  bb_0036D738 -->|fallthrough| bb_0036D77F
  bb_0036D817 -->|flow| bb_0036D818
  bb_0036D818 -->|branch| bb_0036D77F
```
