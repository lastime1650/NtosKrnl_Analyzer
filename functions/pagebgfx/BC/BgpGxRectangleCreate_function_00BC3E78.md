# BgpGxRectangleCreate

- RVA: `0x00BC3E78`–`0x00BC3EFB` (길이 `131` bytes)
- VA: `0x0000000140BC3E78`
- 실행 섹션: `PAGEBGFX`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B020`
- 디코드: `41`개 명령, `131/131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BC3EA4` → [GxpBitsToBytes](../../text/4C/GxpBitsToBytes_function_004C74F0.md) (function, `0x004C74F0`)
- `0x00BC3EAE` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (function, `0x003E4374`)

### Direct callers
- [BgpGxConvertRectangleEx](../../text/46/BgpGxConvertRectangleEx_function_004696D4.md) at `0x0046972B`
- [BgpGxParseBitmap](BgpGxParseBitmap_function_00BC00B8.md) at `0x00BC0118`
- [BgpGxBlendRectangle](BgpGxBlendRectangle_function_00BC2400.md) at `0x00BC24C2`
- [BgpTxtCreateRegion](BgpTxtCreateRegion_function_00BC2908.md) at `0x00BC2A8B`
- [BgpTxtCreateRegion](BgpTxtCreateRegion_function_00BC2908.md) at `0x00BC2AB8`
- [BgpTxtDisplayString](BgpTxtDisplayString_function_00BC2BB0.md) at `0x00BC2CB6`
- [AnFwDisplayFade](AnFwDisplayFade_function_00BC36EC.md) at `0x00BC3A8F`
- [BgpGxReadRectangle](BgpGxReadRectangle_function_00BC3D18.md) at `0x00BC3D49`
- [BgpGxFindSubRectangle](BgpGxFindSubRectangle_function_00BC4168.md) at `0x00BC4270`
- [sub_00BC65EE](Unknown_function_00BC65EE.md) at `0x00BC66C1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BC3EA4` → [GxpBitsToBytes](../../text/4C/GxpBitsToBytes_function_004C74F0.md) (`PAGEBGFX` → `.text`)
  - `0x00BC3EAE` → [BgpFwAllocateMemory](../../text/3E/BgpFwAllocateMemory_function_003E4374.md) (`PAGEBGFX` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BC3E78  48 8B C4                        mov rax, rsp
00BC3E7B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00BC3E7F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00BC3E83  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00BC3E87  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00BC3E8B  41 56                           push r14
00BC3E8D  48 83 EC 20                     sub rsp, 0x20
00BC3E91  48 8B F9                        mov rdi, rcx
00BC3E94  33 DB                           xor ebx, ebx
00BC3E96  8B CA                           mov ecx, edx
00BC3E98  4D 8B F0                        mov r14, r8
00BC3E9B  8B F2                           mov esi, edx
00BC3E9D  0F AF 0F                        imul ecx, dword ptr [rdi]
00BC3EA0  0F AF 4F 04                     imul ecx, dword ptr [rdi + 4]
00BC3EA4  E8 47 36 90 FF                  call 0x1404c74f0
00BC3EA9  8B E8                           mov ebp, eax
00BC3EAB  8D 48 48                        lea ecx, [rax + 0x48]
00BC3EAE  E8 C1 04 82 FF                  call 0x1403e4374
00BC3EB3  48 85 C0                        test rax, rax
00BC3EB6  74 3C                           je 0x140bc3ef4
00BC3EB8  8B 4F 04                        mov ecx, dword ptr [rdi + 4]
00BC3EBB  89 08                           mov dword ptr [rax], ecx
00BC3EBD  8B 0F                           mov ecx, dword ptr [rdi]
00BC3EBF  89 48 04                        mov dword ptr [rax + 4], ecx
00BC3EC2  48 8D 48 48                     lea rcx, [rax + 0x48]
00BC3EC6  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
00BC3ECA  89 70 08                        mov dword ptr [rax + 8], esi
00BC3ECD  89 58 10                        mov dword ptr [rax + 0x10], ebx
00BC3ED0  89 68 0C                        mov dword ptr [rax + 0xc], ebp
00BC3ED3  49 89 06                        mov qword ptr [r14], rax
00BC3ED6  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00BC3EDB  8B C3                           mov eax, ebx
00BC3EDD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BC3EE2  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00BC3EE7  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
00BC3EEC  48 83 C4 20                     add rsp, 0x20
00BC3EF0  41 5E                           pop r14
00BC3EF2  C3                              ret
00BC3EF3  CC                              int3
00BC3EF4  BB 17 00 00 C0                  mov ebx, 0xc0000017
00BC3EF9  EB DB                           jmp 0x140bc3ed6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgpGxRectangleCreate(__int64 a1, int a2, __int64 a3)
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
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    a1 = (unsigned int)(((unsigned int)(a2)) * (*(unsigned int *)(a1)));
    a1 = (unsigned int)((a1) * (*(unsigned int *)(a1 + 4)));
    result = GxpBitsToBytes(a1, a2, a3, a4);
    result = BgpFwAllocateMemory(result + 72, a2, a3, a4);
    if (result == 0) goto loc_00BC3EF4;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned int *)(result + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    *(unsigned __int64 *)(result + 24) = result + 72;
    *(unsigned int *)(result + 8) = (unsigned int)((unsigned int)(a2));
    *(unsigned int *)(result + 16) = 0;
    *(unsigned int *)(result + 12) = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned __int64 *)(a3) = result;
loc_00BC3ED6:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_00BC3EF4:
    goto loc_00BC3ED6;
}
```

## 5. (Beta) C Style

```c
int64_t BgpGxRectangleCreate(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

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
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    Arg1 = (uint32_t)(((uint32_t)(Arg2)) * (*(uint32_t *)(arg1)));
    Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(arg1 + 0x4)));
    result = GxpBitsToBytes(Arg1, Arg2, Arg3, a4);
    result = BgpFwAllocateMemory(result + 72, Arg2, Arg3, a4);
    if (result == 0) goto loc_00BC3EF4;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    *(uint32_t *)(result + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
    *(uint64_t *)(result + 0x18) = result + 72;
    *(uint32_t *)(result + 0x8) = (uint32_t)((uint32_t)(Arg2));
    *(uint32_t *)(result + 0x10) = 0;
    *(uint32_t *)(result + 0xC) = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint64_t *)(arg3) = result;
loc_00BC3ED6:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_00BC3EF4:
    goto loc_00BC3ED6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagebgfx&rva=0x00BC3E78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BC3E78[BB_00BC3E78]
  bb_00BC3EB8[BB_00BC3EB8]
  bb_00BC3ED6[BB_00BC3ED6]
  bb_00BC3EF3[BB_00BC3EF3]
  bb_00BC3EF4[BB_00BC3EF4]
  bb_00BC3E78 -->|branch| bb_00BC3EF4
  bb_00BC3E78 -->|fallthrough| bb_00BC3EB8
  bb_00BC3EB8 -->|flow| bb_00BC3ED6
  bb_00BC3EF3 -->|flow| bb_00BC3EF4
  bb_00BC3EF4 -->|branch| bb_00BC3ED6
```
