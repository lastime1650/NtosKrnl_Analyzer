# KiVerifyXcpt2

- RVA: `0x00C3AB10`–`0x00C3AB58` (길이 `72` bytes)
- VA: `0x0000000140C3AB10`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB13C`
- 디코드: `23`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiVerifyXcpt15](../BE/KiVerifyXcpt15_function_00BEF260.md) at `0x00BEF26F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3AB10  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00C3AB15  48 83 EC 38                     sub rsp, 0x38
00C3AB19  48 89 64 24 20                  mov qword ptr [rsp + 0x20], rsp
00C3AB1E  48 8B D1                        mov rdx, rcx
00C3AB21  83 79 08 01                     cmp dword ptr [rcx + 8], 1
00C3AB25  74 0D                           je 0x140c3ab34
00C3AB27  83 49 0C FF                     or dword ptr [rcx + 0xc], 0xffffffff
00C3AB2B  C7 41 10 01 00 00 00            mov dword ptr [rcx + 0x10], 1
00C3AB32  EB 16                           jmp 0x140c3ab4a
00C3AB34  48 8B 01                        mov rax, qword ptr [rcx]
00C3AB37  FF 00                           inc dword ptr [rax]
00C3AB39  90                              nop
00C3AB3A  EB 0E                           jmp 0x140c3ab4a
00C3AB3C  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00C3AB41  48 8B 02                        mov rax, qword ptr [rdx]
00C3AB44  8B 08                           mov ecx, dword ptr [rax]
00C3AB46  FF C1                           inc ecx
00C3AB48  89 08                           mov dword ptr [rax], ecx
00C3AB4A  48 63 42 0C                     movsxd rax, dword ptr [rdx + 0xc]
00C3AB4E  48 01 42 18                     add qword ptr [rdx + 0x18], rax
00C3AB52  48 83 C4 38                     add rsp, 0x38
00C3AB56  C3                              ret
00C3AB57  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt2(__int64 a1)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (56);
    v_stack_m18 = v_rsp;
    if ((*(unsigned int *)(a1 + 8)) == 1) goto loc_00C3AB34;
    *(unsigned int *)(a1 + 16) = 1;
    goto loc_00C3AB4A;
loc_00C3AB34:
    goto loc_00C3AB4A;
loc_00C3AB4A:
    v_rsp = (v_rsp) + (56);
    return (int)(*(unsigned int *)(a1 + 12));
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt2(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (56);
    v_stack_m18 = local_rsp;
    if ((*(uint32_t *)(arg1 + 0x8)) == 1) goto loc_00C3AB34;
    *(uint32_t *)(arg1 + 0x10) = 1;
    goto loc_00C3AB4A;
loc_00C3AB34:
    goto loc_00C3AB4A;
loc_00C3AB4A:
    local_rsp = (local_rsp) + (56);
    return (int32_t)(*(uint32_t *)(arg1 + 0xC));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3AB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3AB10[BB_00C3AB10]
  bb_00C3AB27[BB_00C3AB27]
  bb_00C3AB34[BB_00C3AB34]
  bb_00C3AB3C[BB_00C3AB3C]
  bb_00C3AB4A[BB_00C3AB4A]
  bb_00C3AB57[BB_00C3AB57]
  bb_00C3AB10 -->|branch| bb_00C3AB34
  bb_00C3AB10 -->|fallthrough| bb_00C3AB27
  bb_00C3AB27 -->|branch| bb_00C3AB4A
  bb_00C3AB34 -->|branch| bb_00C3AB4A
  bb_00C3AB3C -->|flow| bb_00C3AB4A
```
