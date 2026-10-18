# PopQueryBootSessionStandbyActivationInfo

- RVA: `0x0043AD74`–`0x0043ADC3` (길이 `79` bytes)
- VA: `0x000000014043AD74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `23`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0043AD9A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0043ADA5` → [PpmQueryPlatformStateResidency](PpmQueryPlatformStateResidency_function_0043AEF4.md) (function, `0x0043AEF4`)

### Direct callers
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8BD5F`

### Static image references
- `0x0043AD7E` → RVA `0x00E677C8` (`.data`; read)
- `0x0043AD9F` → RVA `0x00E27EC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043AD74  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0043AD79  57                              push rdi
0043AD7A  48 83 EC 20                     sub rsp, 0x20
0043AD7E  48 8B 05 43 CA A2 00            mov rax, qword ptr [rip + 0xa2ca43]
0043AD85  33 DB                           xor ebx, ebx
0043AD87  48 8B F9                        mov rdi, rcx
0043AD8A  48 85 C0                        test rax, rax
0043AD8D  74 2D                           je 0x14043adbc
0043AD8F  48 8D 51 10                     lea rdx, [rcx + 0x10]
0043AD93  4C 8B C7                        mov r8, rdi
0043AD96  48 83 C1 18                     add rcx, 0x18
0043AD9A  E8 31 FD 27 00                  call 0x1406baad0
0043AD9F  8B 0D 1B D1 9E 00               mov ecx, dword ptr [rip + 0x9ed11b]
0043ADA5  E8 4A 01 00 00                  call 0x14043aef4
0043ADAA  48 89 47 08                     mov qword ptr [rdi + 8], rax
0043ADAE  8B C3                           mov eax, ebx
0043ADB0  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0043ADB5  48 83 C4 20                     add rsp, 0x20
0043ADB9  5F                              pop rdi
0043ADBA  C3                              ret
0043ADBB  CC                              int3
0043ADBC  BB 02 00 00 C0                  mov ebx, 0xc0000002
0043ADC1  EB EB                           jmp 0x14043adae
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopQueryBootSessionStandbyActivationInfo(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    if (*(unsigned __int64 *)(v_rip + 10668611) == 0) goto loc_0043ADBC;
    a1 = (a1) + (24);
    result = guard_dispatch_icall(a1, a1 + 16, a1, a4);
    result = PpmQueryPlatformStateResidency((unsigned int)(*(unsigned int *)(v_rip + 10408219)), a1 + 16, a1, a4);
    *(unsigned __int64 *)(a1 + 8) = result;
loc_0043ADAE:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_0043ADBC:
    goto loc_0043ADAE;
}
```

## 5. (Beta) C Style

```c
int64_t PopQueryBootSessionStandbyActivationInfo(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    if (*(uint64_t *)(v_rip + 0xA2CA43) == 0) goto loc_0043ADBC;
    Arg1 = (Arg1) + (24);
    result = guard_dispatch_icall(Arg1, Arg1 + 16, Arg1, a4);
    result = PpmQueryPlatformStateResidency((uint32_t)(*(uint32_t *)(v_rip + 0x9ED11B)), Arg1 + 16, Arg1, a4);
    *(uint64_t *)(arg1 + 0x8) = result;
loc_0043ADAE:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_0043ADBC:
    goto loc_0043ADAE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043AD74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043AD74[BB_0043AD74]
  bb_0043AD8F[BB_0043AD8F]
  bb_0043ADAE[BB_0043ADAE]
  bb_0043ADBB[BB_0043ADBB]
  bb_0043ADBC[BB_0043ADBC]
  bb_0043AD74 -->|branch| bb_0043ADBC
  bb_0043AD74 -->|fallthrough| bb_0043AD8F
  bb_0043AD8F -->|flow| bb_0043ADAE
  bb_0043ADBB -->|flow| bb_0043ADBC
  bb_0043ADBC -->|branch| bb_0043ADAE
```
