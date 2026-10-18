# ObpInsertDirectoryEntry

- RVA: `0x00A18AC0`–`0x00A18B6B` (길이 `171` bytes)
- VA: `0x0000000140A18AC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA1E4`
- 디코드: `46`개 명령, `171/171` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A18AEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A18B03` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00A18B2F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)

### Direct callers
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089D85D`
- [ObCreateObjectTypeEx](../AB/ObCreateObjectTypeEx_function_00AB46D0.md) at `0x00AB4C75`
- [ObInitSystem](../../init/C7/ObInitSystem_function_00C71C7C.md) at `0x00C722D5`

### Static image references
- `0x00A18B3C` → RVA `0x00F0FF80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A18AEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A18B03` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00A18B2F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A18AC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A18AC5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A18ACA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
00A18ACF  41 56                           push r14
00A18AD1  48 83 EC 20                     sub rsp, 0x20
00A18AD5  49 8B F8                        mov rdi, r8
00A18AD8  48 8B F2                        mov rsi, rdx
00A18ADB  4C 8B F1                        mov r14, rcx
00A18ADE  BA 18 00 00 00                  mov edx, 0x18
00A18AE3  B9 00 01 00 00                  mov ecx, 0x100
00A18AE8  41 B8 4F 62 44 69               mov r8d, 0x6944624f
00A18AEE  E8 FD 95 16 00                  call 0x140b820f0
00A18AF3  48 8B D8                        mov rbx, rax
00A18AF6  48 85 C0                        test rax, rax
00A18AF9  74 6E                           je 0x140a18b69
00A18AFB  BA 4F 62 44 69                  mov edx, 0x6944624f
00A18B00  48 8B CE                        mov rcx, rsi
00A18B03  E8 08 7C 7F FF                  call 0x140210710
00A18B08  0F B6 47 14                     movzx eax, byte ptr [rdi + 0x14]
00A18B0C  BA 4F 62 44 69                  mov edx, 0x6944624f
00A18B11  49 8D 0C C6                     lea rcx, [r14 + rax*8]
00A18B15  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00A18B18  89 43 10                        mov dword ptr [rbx + 0x10], eax
00A18B1B  48 8B 01                        mov rax, qword ptr [rcx]
00A18B1E  48 89 03                        mov qword ptr [rbx], rax
00A18B21  48 89 19                        mov qword ptr [rcx], rbx
00A18B24  48 89 73 08                     mov qword ptr [rbx + 8], rsi
00A18B28  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
00A18B2C  49 8B CE                        mov rcx, r14
00A18B2F  E8 DC 7B 7F FF                  call 0x140210710
00A18B34  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00A18B38  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
00A18B3C  48 8D 15 3D 74 4F 00            lea rdx, [rip + 0x4f743d]
00A18B43  83 E0 03                        and eax, 3
00A18B46  0F B6 04 10                     movzx eax, byte ptr [rax + rdx]
00A18B4A  48 2B C8                        sub rcx, rax
00A18B4D  B0 01                           mov al, 1
00A18B4F  4C 89 31                        mov qword ptr [rcx], r14
00A18B52  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A18B57  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00A18B5C  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00A18B61  48 83 C4 20                     add rsp, 0x20
00A18B65  41 5E                           pop r14
00A18B67  C3                              ret
00A18B68  CC                              int3
00A18B69  EB E7                           jmp 0x140a18b52
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpInsertDirectoryEntry(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    result = ExAllocatePool2(256, 24, (unsigned int)(0x6944624FULL), a4);
    if (result == 0) goto loc_00A18B69;
    result = ObfReferenceObjectWithTag(a2, (unsigned int)(0x6944624FULL), (unsigned int)(0x6944624FULL), a4);
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 16)));
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a3 + 20) * 8);
    *(unsigned __int64 *)(a1 + *(unsigned __int8 *)(a3 + 20) * 8) = result;
    *(unsigned __int64 *)(result + 8) = a2;
    *(unsigned __int64 *)(a3 + 8) = a1 + *(unsigned __int8 *)(a3 + 20) * 8;
    result = ObfReferenceObjectWithTag(a1, (unsigned int)(0x6944624FULL), (unsigned int)(0x6944624FULL), a4);
    result = (unsigned int)((*(unsigned __int8 *)(a2 - 48 + 26)) & (3));
    a1 = (a2 - 48) - (*(unsigned __int8 *)(result + v_rip + 5207101 * 1));
    *(unsigned __int64 *)(a1) = a1;
loc_00A18B52:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_00A18B69:
    goto loc_00A18B52;
}
```

## 5. (Beta) C Style

```c
int64_t ObpInsertDirectoryEntry(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    result = ExAllocatePool2(256, 24, (uint32_t)(0x6944624FULL), a4);
    if (result == 0) goto loc_00A18B69;
    result = ObfReferenceObjectWithTag(Arg2, (uint32_t)(0x6944624FULL), (uint32_t)(0x6944624FULL), a4);
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg3 + 0x10)));
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + *(uint8_t *)(arg3 + 0x14) * 8);
    *(uint64_t *)(arg1 + *(uint8_t *)(arg3 + 0x14) * 8) = result;
    *(void **)(result + 0x8) = Arg2;
    *(void **)(arg3 + 0x8) = Arg1 + *(uint8_t *)(arg3 + 0x14) * 8;
    result = ObfReferenceObjectWithTag(Arg1, (uint32_t)(0x6944624FULL), (uint32_t)(0x6944624FULL), a4);
    result = (uint32_t)((*(uint8_t *)(arg2 - 0x30 + 0x1A)) & (3));
    Arg1 = (Arg2 - 48) - (*(uint8_t *)(result + v_rip + 0x4F743D * 1));
    *(void **)(arg1) = Arg1;
loc_00A18B52:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_00A18B69:
    goto loc_00A18B52;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rax*8` | `64` | `R` |
| `Arg2` | `- 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x1A` | `8` | `R` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x14` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A18AC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A18AC0[BB_00A18AC0]
  bb_00A18AFB[BB_00A18AFB]
  bb_00A18B52[BB_00A18B52]
  bb_00A18B68[BB_00A18B68]
  bb_00A18B69[BB_00A18B69]
  bb_00A18AC0 -->|branch| bb_00A18B69
  bb_00A18AC0 -->|fallthrough| bb_00A18AFB
  bb_00A18AFB -->|flow| bb_00A18B52
  bb_00A18B68 -->|flow| bb_00A18B69
  bb_00A18B69 -->|branch| bb_00A18B52
```
