# RtlInitializeSystemOverrideDelta

- RVA: `0x00AACFB0`–`0x00AAD024` (길이 `116` bytes)
- VA: `0x0000000140AACFB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC044`
- 디코드: `29`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlApplyFunctionOverrideFixupsToImage](../79/RtlApplyFunctionOverrideFixupsToImage_function_007954E0.md) at `0x007955AC`
- [MiRelocateImage](../98/MiRelocateImage_function_00988E14.md) at `0x0098958D`

### Static image references
- `0x00AACFC2` → RVA `0x00E375B0` (`.data`; read)
- `0x00AACFC8` → RVA `0x00E375AC` (`.data`; read)
- `0x00AACFCE` → RVA `0x00E2D830` (`.data`; read)
- `0x00AAD008` → RVA `0x00E2D8A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AACFB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AACFB5  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00AACFBA  48 8B F9                        mov rdi, rcx
00AACFBD  4D 85 C9                        test r9, r9
00AACFC0  75 2C                           jne 0x140aacfee
00AACFC2  8B 05 E8 A5 38 00               mov eax, dword ptr [rip + 0x38a5e8]
00AACFC8  03 05 DE A5 38 00               add eax, dword ptr [rip + 0x38a5de]
00AACFCE  48 8B 0D 5B 08 38 00            mov rcx, qword ptr [rip + 0x38085b]
00AACFD5  41 03 C0                        add eax, r8d
00AACFD8  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
00AACFDD  48 2B C8                        sub rcx, rax
00AACFE0  48 2B CA                        sub rcx, rdx
00AACFE3  48 89 4F 10                     mov qword ptr [rdi + 0x10], rcx
00AACFE7  48 8B 7C 24 10                  mov rdi, qword ptr [rsp + 0x10]
00AACFEC  C3                              ret
00AACFED  CC                              int3
00AACFEE  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
00AACFF2  45 8D 90 FF 0F 00 00            lea r10d, [r8 + 0xfff]
00AACFF9  B9 00 F0 FF FF                  mov ecx, 0xfffff000
00AACFFE  05 FF 0F 00 00                  add eax, 0xfff
00AAD003  44 23 D1                        and r10d, ecx
00AAD006  23 C8                           and ecx, eax
00AAD008  44 03 15 91 08 38 00            add r10d, dword ptr [rip + 0x380891]
00AAD00F  03 0D 8B 08 38 00               add ecx, dword ptr [rip + 0x38088b]
00AAD015  4C 03 D2                        add r10, rdx
00AAD018  49 2B CA                        sub rcx, r10
00AAD01B  49 03 C9                        add rcx, r9
00AAD01E  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00AAD022  EB 9E                           jmp 0x140aacfc2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlInitializeSystemOverrideDelta(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    if (a4 != 0) goto loc_00AACFEE;
loc_00AACFC2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3712488))) + (*(unsigned int *)(v_rip + 3712478)));
    result = (unsigned int)((result) + ((unsigned int)(a3)));
    a1 = (*(unsigned __int64 *)(v_rip + 3672155)) - (result);
    a1 = (a1) - (a2);
    *(unsigned __int64 *)(a1 + 16) = a1;
    return result;
loc_00AACFEE:
    result = (unsigned int)(((unsigned int)(a5)) + (0xFFFULL));
    v_r10 = (unsigned int)((a3 + 4095) & ((unsigned int)((unsigned int)(0xFFFFF000ULL))));
    a1 = (unsigned int)(((unsigned int)(0xFFFFF000ULL)) & ((unsigned int)(result)));
    v_r10 = (unsigned int)((v_r10) + (*(unsigned int *)(v_rip + 3672209)));
    a1 = (unsigned int)((a1) + (*(unsigned int *)(v_rip + 3672203)));
    v_r10 = (v_r10) + (a2);
    a1 = (a1) - (v_r10);
    a1 = (a1) + (a4);
    *(unsigned __int64 *)(v_stack_p10 + 8) = a1;
    goto loc_00AACFC2;
}
```

## 5. (Beta) C Style

```c
int64_t RtlInitializeSystemOverrideDelta(void *SystemOverrideDelta, int64_t Arg2, void *Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *systemOverrideDelta = (uint8_t *)SystemOverrideDelta;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    if (Arg4 != 0) goto loc_00AACFEE;
loc_00AACFC2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x38A5E8))) + (*(uint32_t *)(v_rip + 0x38A5DE)));
    result = (uint32_t)((result) + ((uint32_t)(Arg3)));
    SystemOverrideDelta = (*(uint64_t *)(v_rip + 0x38085B)) - (result);
    SystemOverrideDelta = (SystemOverrideDelta) - (Arg2);
    *(void **)(systemOverrideDelta + 0x10) = SystemOverrideDelta;
    return result;
loc_00AACFEE:
    result = (uint32_t)(((uint32_t)(Arg5)) + (0xFFFULL));
    local_r10 = (uint32_t)((Arg3 + 4095) & ((uint32_t)((uint32_t)(0xFFFFF000ULL))));
    SystemOverrideDelta = (uint32_t)(((uint32_t)(0xFFFFF000ULL)) & ((uint32_t)(result)));
    local_r10 = (uint32_t)((local_r10) + (*(uint32_t *)(v_rip + 0x380891)));
    SystemOverrideDelta = (uint32_t)((SystemOverrideDelta) + (*(uint32_t *)(v_rip + 0x38088B)));
    local_r10 = (local_r10) + (Arg2);
    SystemOverrideDelta = (SystemOverrideDelta) - (local_r10);
    SystemOverrideDelta = (SystemOverrideDelta) + (Arg4);
    *(void **)(v_stack_p10 + 0x8) = SystemOverrideDelta;
    goto loc_00AACFC2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `SystemOverrideDelta` | `+ 0x8` | `64` | `W` |
| `SystemOverrideDelta` | `+ 0x10` | `64` | `W` |
| `Arg3` | `+ 0xFFF` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AACFB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AACFB0[BB_00AACFB0]
  bb_00AACFC2[BB_00AACFC2]
  bb_00AACFED[BB_00AACFED]
  bb_00AACFEE[BB_00AACFEE]
  bb_00AACFB0 -->|branch| bb_00AACFEE
  bb_00AACFB0 -->|fallthrough| bb_00AACFC2
  bb_00AACFED -->|flow| bb_00AACFEE
  bb_00AACFEE -->|branch| bb_00AACFC2
```
