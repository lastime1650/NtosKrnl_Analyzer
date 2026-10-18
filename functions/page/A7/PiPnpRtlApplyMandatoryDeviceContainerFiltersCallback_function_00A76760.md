# PiPnpRtlApplyMandatoryDeviceContainerFiltersCallback

- RVA: `0x00A76760`–`0x00A767A0` (길이 `64` bytes)
- VA: `0x0000000140A76760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `21`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A76787` → [PiPnpRtlApplyMandatoryDeviceFilters](../8E/PiPnpRtlApplyMandatoryDeviceFilters_function_008E5E90.md) (function, `0x008E5E90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A76760  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A76765  57                              push rdi
00A76766  48 83 EC 30                     sub rsp, 0x30
00A7676A  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
00A7676E  48 8D 5A 10                     lea rbx, [rdx + 0x10]
00A76772  48 8B C2                        mov rax, rdx
00A76775  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A7677A  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00A7677E  49 8B F8                        mov rdi, r8
00A76781  45 33 C0                        xor r8d, r8d
00A76784  48 8B 08                        mov rcx, qword ptr [rax]
00A76787  E8 04 F7 E6 FF                  call 0x1408e5e90
00A7678C  85 C0                           test eax, eax
00A7678E  78 04                           js 0x140a76794
00A76790  8A 0B                           mov cl, byte ptr [rbx]
00A76792  88 0F                           mov byte ptr [rdi], cl
00A76794  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A76799  48 83 C4 30                     add rsp, 0x30
00A7679D  5F                              pop rdi
00A7679E  C3                              ret
00A7679F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlApplyMandatoryDeviceContainerFiltersCallback(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = a2 + 16;
    a3 = 0;
    result = PiPnpRtlApplyMandatoryDeviceFilters(*(unsigned __int64 *)(a2), *(unsigned __int64 *)(a1 + 16), a3, *(unsigned __int64 *)(a2 + 8));
    if (!(sign_flag)) {
        a1 = *(unsigned __int8 *)(a2 + 16);
        *(unsigned __int8 *)(a3) = (unsigned __int8)(a1);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiPnpRtlApplyMandatoryDeviceContainerFiltersCallback(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = Arg2 + 16;
    Arg3 = 0;
    result = PiPnpRtlApplyMandatoryDeviceFilters(*(uint64_t *)(arg2), *(uint64_t *)(arg1 + 0x10), Arg3, *(uint64_t *)(arg2 + 0x8));
    if (!(sign_flag)) {
        Arg1 = *(uint8_t *)(arg2 + 0x10);
        *(uint8_t *)(arg3) = (uint8_t)(Arg1);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A76760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A76760[BB_00A76760]
  bb_00A76790[BB_00A76790]
  bb_00A76794[BB_00A76794]
  bb_00A7679F[BB_00A7679F]
  bb_00A76760 -->|branch| bb_00A76794
  bb_00A76760 -->|fallthrough| bb_00A76790
  bb_00A76790 -->|flow| bb_00A76794
```
