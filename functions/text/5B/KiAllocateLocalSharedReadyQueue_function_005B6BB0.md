# KiAllocateLocalSharedReadyQueue

- RVA: `0x005B6BB0`–`0x005B6C24` (길이 `116` bytes)
- VA: `0x00000001405B6BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `28`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B6C00` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (function, `0x00B84270`)

### Direct callers
- [KiStartDynamicProcessor](../../page/74/KiStartDynamicProcessor_function_007456C8.md) at `0x00745995`
- [KeStartAllProcessors](../../init/C3/KeStartAllProcessors_function_00C36F78.md) at `0x00C372ED`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005B6C00` → [ExAllocatePool3](../../poolcode/B8/ExAllocatePool3_function_00B84270.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B6BB0  40 53                           push rbx
005B6BB2  48 83 EC 40                     sub rsp, 0x40
005B6BB6  48 8B 81 C0 00 00 00            mov rax, qword ptr [rcx + 0xc0]
005B6BBD  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
005B6BC2  0F 57 C0                        xorps xmm0, xmm0
005B6BC5  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
005B6BCD  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
005B6BD2  48 8B D9                        mov rbx, rcx
005B6BD5  C6 44 24 30 03                  mov byte ptr [rsp + 0x30], 3
005B6BDA  0F B7 90 8A 00 00 00            movzx edx, word ptr [rax + 0x8a]
005B6BE1  B9 48 00 00 00                  mov ecx, 0x48
005B6BE6  48 0F BA 6C 24 30 08            bts qword ptr [rsp + 0x30], 8
005B6BED  0F BA EA 1F                     bts edx, 0x1f
005B6BF1  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
005B6BF5  41 B8 4B 69 53 51               mov r8d, 0x5153694b
005B6BFB  BA 00 07 00 00                  mov edx, 0x700
005B6C00  E8 6B D6 5C 00                  call 0x140b84270
005B6C05  48 8B C8                        mov rcx, rax
005B6C08  33 C0                           xor eax, eax
005B6C0A  48 85 C9                        test rcx, rcx
005B6C0D  75 07                           jne 0x1405b6c16
005B6C0F  B8 9A 00 00 C0                  mov eax, 0xc000009a
005B6C14  EB 07                           jmp 0x1405b6c1d
005B6C16  48 89 8B 00 94 00 00            mov qword ptr [rbx + 0x9400], rcx
005B6C1D  48 83 C4 40                     add rsp, 0x40
005B6C21  5B                              pop rbx
005B6C22  C3                              ret
005B6C23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAllocateLocalSharedReadyQueue(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_stack_m28 = 1;
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 3;
    v_stack_m10 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 138));
    result = ExAllocatePool3(72, (unsigned int)(0x700ULL), (unsigned int)(0x5153694BULL), v_stack_m18);
    result = 0;
    if (0 != 0) goto loc_005B6C16;
    goto loc_005B6C1D;
loc_005B6C16:
    *(unsigned __int64 *)(a1 + 37888) = 0;
loc_005B6C1D:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(0xC000009AULL);
}
```

## 5. (Beta) C Style

```c
int64_t KiAllocateLocalSharedReadyQueue(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    v_stack_m28 = 1;
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 3;
    v_stack_m10 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8A));
    result = ExAllocatePool3(72, (uint32_t)(0x700ULL), (uint32_t)(0x5153694BULL), v_stack_m18);
    result = 0;
    if (0 != 0) goto loc_005B6C16;
    goto loc_005B6C1D;
loc_005B6C16:
    *(uint64_t *)(arg1 + 0x9400) = 0;
loc_005B6C1D:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(0xC000009AULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0x9400` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B6BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B6BB0[BB_005B6BB0]
  bb_005B6C0F[BB_005B6C0F]
  bb_005B6C16[BB_005B6C16]
  bb_005B6C1D[BB_005B6C1D]
  bb_005B6C23[BB_005B6C23]
  bb_005B6BB0 -->|branch| bb_005B6C16
  bb_005B6BB0 -->|fallthrough| bb_005B6C0F
  bb_005B6C0F -->|branch| bb_005B6C1D
  bb_005B6C16 -->|flow| bb_005B6C1D
```
