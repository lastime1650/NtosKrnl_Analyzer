# MiPromoteControlAreaToStrongCode

- RVA: `0x0080720C`–`0x00807272` (길이 `102` bytes)
- VA: `0x000000014080720C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065960`
- 디코드: `31`개 명령, `102/102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00807240` → [MiValidateSectionCreate](../94/MiValidateSectionCreate_function_00940190.md) (function, `0x00940190`)
- `0x00807254` → [MiGetSectionStrongImageReference](../93/MiGetSectionStrongImageReference_function_0093E9C0.md) (function, `0x0093E9C0`)

### Direct callers
- [MiLoadHotPatch](../AB/MiLoadHotPatch_function_00AB521C.md) at `0x00AB544D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0080720C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00807211  57                              push rdi
00807212  48 83 EC 40                     sub rsp, 0x40
00807216  41 0F BA E8 1E                  bts r8d, 0x1e
0080721B  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00807220  48 8B C2                        mov rax, rdx
00807223  C6 44 24 28 0C                  mov byte ptr [rsp + 0x28], 0xc
00807228  44 89 44 24 20                  mov dword ptr [rsp + 0x20], r8d
0080722D  49 8B F9                        mov rdi, r9
00807230  48 8B D9                        mov rbx, rcx
00807233  48 8B D1                        mov rdx, rcx
00807236  41 83 C8 FF                     or r8d, 0xffffffff
0080723A  45 33 C9                        xor r9d, r9d
0080723D  48 8B C8                        mov rcx, rax
00807240  E8 4B 8F 13 00                  call 0x140940190
00807245  85 C0                           test eax, eax
00807247  78 1D                           js 0x140807266
00807249  48 8B 5B 60                     mov rbx, qword ptr [rbx + 0x60]
0080724D  48 83 E3 F8                     and rbx, 0xfffffffffffffff8
00807251  48 8B CB                        mov rcx, rbx
00807254  E8 67 77 13 00                  call 0x14093e9c0
00807259  85 C0                           test eax, eax
0080725B  78 09                           js 0x140807266
0080725D  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00807261  48 89 07                        mov qword ptr [rdi], rax
00807264  33 C0                           xor eax, eax
00807266  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0080726B  48 83 C4 40                     add rsp, 0x40
0080726F  5F                              pop rdi
00807270  C3                              ret
00807271  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPromoteControlAreaToStrongCode(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned __int8 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (64);
    v_stack_m18 = 1;
    v_stack_m20 = 12;
    v_stack_m28 = a3;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    a4 = 0;
    result = MiValidateSectionCreate(a2, a1, a3, a4);
    if (sign_flag) goto loc_00807266;
    v_rbx = (*(unsigned __int64 *)(a1 + 96)) & (-8);
    result = MiGetSectionStrongImageReference(v_rbx, a1, a3, a4);
    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(v_rbx + 64);
        *(unsigned __int64 *)(a4) = result;
        result = 0;
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiPromoteControlAreaToStrongCode(void *Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint8_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (64);
    v_stack_m18 = 1;
    v_stack_m20 = 12;
    v_stack_m28 = Arg3;
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    Arg4 = 0;
    result = MiValidateSectionCreate(Arg2, Arg1, Arg3, Arg4);
    if (sign_flag) goto loc_00807266;
    local_rbx = (*(uint64_t *)(arg1 + 0x60)) & (-8);
    result = MiGetSectionStrongImageReference(local_rbx, Arg1, Arg3, Arg4);
    if (!(sign_flag)) {
        result = *(uint64_t *)(local_rbx + 0x40);
        *(uint64_t *)(arg4) = result;
        result = 0;
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0080720C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0080720C[BB_0080720C]
  bb_00807249[BB_00807249]
  bb_0080725D[BB_0080725D]
  bb_00807266[BB_00807266]
  bb_00807271[BB_00807271]
  bb_0080720C -->|branch| bb_00807266
  bb_0080720C -->|fallthrough| bb_00807249
  bb_00807249 -->|branch| bb_00807266
  bb_00807249 -->|fallthrough| bb_0080725D
  bb_0080725D -->|flow| bb_00807266
```
