# KeGetNodePrimarySubNode

- RVA: `0x0043EFF4`–`0x0043F057` (길이 `99` bytes)
- VA: `0x000000014043EFF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4BB4`
- 디코드: `27`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0043F023` → [RtlCopyVolatileMemory](../6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x0043F02D` → [KeIsEmptyGroupMask](../25/KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x0043F047` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeQueryLogicalProcessorRelationship](../2C/KeQueryLogicalProcessorRelationship_function_002CEA60.md) at `0x002CF59C`
- [MiGetClosestNodeWithProcessors](MiGetClosestNodeWithProcessors_function_0043EEE0.md) at `0x0043EF32`
- [KeQueryNodeActiveAffinity](KeQueryNodeActiveAffinity_function_0043EF80.md) at `0x0043EFC2`
- [KiComputeNumaCosts](../../init/C3/KiComputeNumaCosts_function_00C37AD4.md) at `0x00C37CAC`

### Static image references
- `0x0043EFFA` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043EFF4  40 53                           push rbx
0043EFF6  48 83 EC 40                     sub rsp, 0x40
0043EFFA  48 8B 05 3F B7 9C 00            mov rax, qword ptr [rip + 0x9cb73f]
0043F001  48 33 C4                        xor rax, rsp
0043F004  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0043F009  48 8B D9                        mov rbx, rcx
0043F00C  48 8D 51 10                     lea rdx, [rcx + 0x10]
0043F010  0F 57 C0                        xorps xmm0, xmm0
0043F013  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0043F018  41 B8 10 00 00 00               mov r8d, 0x10
0043F01E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0043F023  E8 A8 D9 27 00                  call 0x1406bc9d0
0043F028  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0043F02D  E8 7E 63 E1 FF                  call 0x1402553b0
0043F032  85 C0                           test eax, eax
0043F034  75 1D                           jne 0x14043f053
0043F036  0F B6 43 0C                     movzx eax, byte ptr [rbx + 0xc]
0043F03A  48 8B 44 C3 20                  mov rax, qword ptr [rbx + rax*8 + 0x20]
0043F03F  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0043F044  48 33 CC                        xor rcx, rsp
0043F047  E8 F4 D5 26 00                  call 0x1406ac640
0043F04C  48 83 C4 40                     add rsp, 0x40
0043F050  5B                              pop rbx
0043F051  C3                              ret
0043F052  CC                              int3
0043F053  33 C0                           xor eax, eax
0043F055  EB E8                           jmp 0x14043f03f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGetNodePrimarySubNode(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    result = (*(unsigned __int64 *)(v_rip + 10270527)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m28, a1 + 16, 16, a4);
    result = KeIsEmptyGroupMask(v_stack_m28, a1 + 16, 16, a4);
    if ((unsigned int)(result) != 0) goto loc_0043F053;
loc_0043F03F:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a1 + 16, 16, a4);
    v_rsp = (v_rsp) + (64);
    return result;
loc_0043F053:
    result = 0;
    goto loc_0043F03F;
}
```

## 5. (Beta) C Style

```c
int64_t KeGetNodePrimarySubNode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    result = (*(uint64_t *)(v_rip + 0x9CB73F)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m28 = v_xmm0;
    result = RtlCopyVolatileMemory(v_stack_m28, Arg1 + 16, 16, a4);
    result = KeIsEmptyGroupMask(v_stack_m28, Arg1 + 16, 16, a4);
    if ((uint32_t)(result) != 0) goto loc_0043F053;
loc_0043F03F:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg1 + 16, 16, a4);
    local_rsp = (local_rsp) + (64);
    return result;
loc_0043F053:
    result = 0;
    goto loc_0043F03F;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043EFF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043EFF4[BB_0043EFF4]
  bb_0043F036[BB_0043F036]
  bb_0043F03F[BB_0043F03F]
  bb_0043F052[BB_0043F052]
  bb_0043F053[BB_0043F053]
  bb_0043EFF4 -->|branch| bb_0043F053
  bb_0043EFF4 -->|fallthrough| bb_0043F036
  bb_0043F036 -->|flow| bb_0043F03F
  bb_0043F052 -->|flow| bb_0043F053
  bb_0043F053 -->|branch| bb_0043F03F
```
