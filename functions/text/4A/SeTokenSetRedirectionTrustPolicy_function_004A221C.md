# SeTokenSetRedirectionTrustPolicy

- RVA: `0x004A221C`–`0x004A22AD` (길이 `145` bytes)
- VA: `0x00000001404A221C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B95C`
- 디코드: `37`개 명령, `145/145` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004A2242` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x004A228D` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004A2292` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PspSetRedirectionTrustPolicy](../../page/A7/PspSetRedirectionTrustPolicy_function_00A7C2D4.md) at `0x00A7C2FE`

### Static image references
- `0x004A2264` → RVA `0x00012D08` (`.rdata`; read)
- `0x004A226E` → RVA `0x00E0EBF0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A221C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004A2221  57                              push rdi
004A2222  48 83 EC 20                     sub rsp, 0x20
004A2226  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004A222F  8A DA                           mov bl, dl
004A2231  48 8B F9                        mov rdi, rcx
004A2234  B2 01                           mov dl, 1
004A2236  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004A223D  90                              nop
004A223E  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
004A2242  E8 D9 2B D7 FF                  call 0x140214e20
004A2247  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
004A224C  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
004A2252  84 DB                           test bl, bl
004A2254  74 4D                           je 0x1404a22a3
004A2256  0F BA F0 16                     btr eax, 0x16
004A225A  0F BA E8 17                     bts eax, 0x17
004A225E  89 87 C8 00 00 00               mov dword ptr [rdi + 0xc8], eax
004A2264  48 8B 0D 9D 0A B7 FF            mov rcx, qword ptr [rip - 0x48f563]
004A226B  48 8B C1                        mov rax, rcx
004A226E  F0 48 0F C1 05 79 C9 96 00      lock xadd qword ptr [rip + 0x96c979], rax
004A2277  48 03 C1                        add rax, rcx
004A227A  89 47 38                        mov dword ptr [rdi + 0x38], eax
004A227D  48 C1 E8 20                     shr rax, 0x20
004A2281  89 47 3C                        mov dword ptr [rdi + 0x3c], eax
004A2284  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
004A2289  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
004A228D  E8 7E D7 DB FF                  call 0x14025fa10
004A2292  E8 19 B6 DB FF                  call 0x14025d8b0
004A2297  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004A229C  48 83 C4 20                     add rsp, 0x20
004A22A0  5F                              pop rdi
004A22A1  C3                              ret
004A22A2  CC                              int3
004A22A3  0F BA F0 17                     btr eax, 0x17
004A22A7  0F BA E8 16                     bts eax, 0x16
004A22AB  EB B1                           jmp 0x1404a225e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeTokenSetRedirectionTrustPolicy(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    if (a2 == 0) goto loc_004A22A3;
loc_004A225E:
    *(unsigned int *)(a1 + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200)));
    result = (*(unsigned __int64 *)(v_rip - 4781411)) + (*(unsigned __int64 *)(v_rip - 4781411));
    *(unsigned int *)(a1 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(a1 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004A22A3:
    goto loc_004A225E;
}
```

## 5. (Beta) C Style

```c
int64_t SeTokenSetRedirectionTrustPolicy(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    if (Arg2 == 0) goto loc_004A22A3;
loc_004A225E:
    *(uint32_t *)(arg1 + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8)));
    result = (*(uint64_t *)(v_rip - 0x48F563)) + (*(uint64_t *)(v_rip - 0x48F563));
    *(uint32_t *)(arg1 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(arg1 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), 1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004A22A3:
    goto loc_004A225E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `32` | `W` |
| `Arg1` | `+ 0x3C` | `32` | `W` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A221C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A221C[BB_004A221C]
  bb_004A2256[BB_004A2256]
  bb_004A225E[BB_004A225E]
  bb_004A22A2[BB_004A22A2]
  bb_004A22A3[BB_004A22A3]
  bb_004A221C -->|branch| bb_004A22A3
  bb_004A221C -->|fallthrough| bb_004A2256
  bb_004A2256 -->|flow| bb_004A225E
  bb_004A22A2 -->|flow| bb_004A22A3
  bb_004A22A3 -->|branch| bb_004A225E
```
