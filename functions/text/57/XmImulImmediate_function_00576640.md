# XmImulImmediate

- RVA: `0x00576640`–`0x005766AE` (길이 `110` bytes)
- VA: `0x0000000140576640`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `32`개 명령, `110/110` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00576669` → [XmEvaluateAddressSpecifier](../47/XmEvaluateAddressSpecifier_function_00473224.md) (function, `0x00473224`)
- `0x0057667A` → [XmGetImmediateSourceValue](../47/XmGetImmediateSourceValue_function_0047340C.md) (function, `0x0047340C`)
- `0x00576688` → [XmSetDestinationValue](../47/XmSetDestinationValue_function_004734EC.md) (function, `0x004734EC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00576640  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00576645  57                              push rdi
00576646  48 83 EC 20                     sub rsp, 0x20
0057664A  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
0057664F  48 8B F9                        mov rdi, rcx
00576652  8A 81 8A 00 00 00               mov al, byte ptr [rcx + 0x8a]
00576658  F6 D8                           neg al
0057665A  1B D2                           sbb edx, edx
0057665C  83 E2 02                        and edx, 2
0057665F  FF C2                           inc edx
00576661  89 51 78                        mov dword ptr [rcx + 0x78], edx
00576664  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00576669  E8 B6 CB EF FF                  call 0x140473224
0057666E  8B 57 70                        mov edx, dword ptr [rdi + 0x70]
00576671  48 8B CF                        mov rcx, rdi
00576674  83 E2 02                        and edx, 2
00576677  48 8B D8                        mov rbx, rax
0057667A  E8 8D CD EF FF                  call 0x14047340c
0057667F  48 8B D3                        mov rdx, rbx
00576682  89 47 6C                        mov dword ptr [rdi + 0x6c], eax
00576685  48 8B CF                        mov rcx, rdi
00576688  E8 5F CE EF FF                  call 0x1404734ec
0057668D  8B 54 24 30                     mov edx, dword ptr [rsp + 0x30]
00576691  B8 01 00 00 00                  mov eax, 1
00576696  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0057669B  48 83 C2 06                     add rdx, 6
0057669F  48 8D 14 97                     lea rdx, [rdi + rdx*4]
005766A3  48 89 57 58                     mov qword ptr [rdi + 0x58], rdx
005766A7  48 83 C4 20                     add rsp, 0x20
005766AB  5F                              pop rdi
005766AC  C3                              ret
005766AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmImulImmediate(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 138)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(a1 + 120) = a2;
    result = XmEvaluateAddressSpecifier(a1, v_stack_p8, a3, a4);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 112))) & (2));
    result = XmGetImmediateSourceValue(a1, a2, a3, a4);
    *(unsigned int *)(a1 + 108) = (unsigned int)(result);
    result = XmSetDestinationValue(a1, result, a3, a4);
    a2 = ((unsigned int)(v_stack_p8)) + (6);
    *(unsigned __int64 *)(a1 + 88) = a1 + a2 * 4;
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t XmImulImmediate(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x8A)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(arg1 + 0x78) = Arg2;
    result = XmEvaluateAddressSpecifier(Arg1, v_stack_p8, a3, a4);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x70))) & (2));
    result = XmGetImmediateSourceValue(Arg1, Arg2, a3, a4);
    *(uint32_t *)(arg1 + 0x6C) = (uint32_t)(result);
    result = XmSetDestinationValue(Arg1, result, a3, a4);
    Arg2 = ((uint32_t)(v_stack_p8)) + (6);
    *(void **)(arg1 + 0x58) = Arg1 + Arg2 * 4;
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rdx*4` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x6C` | `32` | `W` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00576640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00576640[BB_00576640]
  bb_005766AD[BB_005766AD]
```
