# CmFcpUsageProviderWorkItemInitialize

- RVA: `0x0066B4B8`–`0x0066B4EF` (길이 `55` bytes)
- VA: `0x000000014066B4B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmFcpInitializeFeatureUsageProviderSubscription](../../page/7F/CmFcpInitializeFeatureUsageProviderSubscription_function_007F530C.md) at `0x007F53AD`

### Static image references
- `0x0066B4BA` → RVA `0x0066B500` (`CmFcpUsageProviderWorkItemWrapper`; read)
- `0x0066B4C9` → RVA `0x00AF7AB0` (`CmFcpFeatureUsageProviderSubscriptionWrapper`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066B4B8  33 D2                           xor edx, edx
0066B4BA  48 8D 05 3F 00 00 00            lea rax, [rip + 0x3f]
0066B4C1  48 89 51 08                     mov qword ptr [rcx + 8], rdx
0066B4C5  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
0066B4C9  48 8D 05 E0 C5 48 00            lea rax, [rip + 0x48c5e0]
0066B4D0  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
0066B4D4  48 89 49 18                     mov qword ptr [rcx + 0x18], rcx
0066B4D8  48 89 11                        mov qword ptr [rcx], rdx
0066B4DB  89 51 28                        mov dword ptr [rcx + 0x28], edx
0066B4DE  48 89 51 20                     mov qword ptr [rcx + 0x20], rdx
0066B4E2  C7 41 2C 04 00 00 00            mov dword ptr [rcx + 0x2c], 4
0066B4E9  4C 89 49 38                     mov qword ptr [rcx + 0x38], r9
0066B4ED  C3                              ret
0066B4EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpUsageProviderWorkItemInitialize(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    a2 = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    *(unsigned __int64 *)(a1 + 16) = v_rip + 63;
    *(unsigned __int64 *)(a1 + 48) = v_rip + 4769248;
    *(unsigned __int64 *)(a1 + 24) = a1;
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned int *)(a1 + 40) = 0;
    *(unsigned __int64 *)(a1 + 32) = 0;
    *(unsigned int *)(a1 + 44) = 4;
    *(unsigned __int64 *)(a1 + 56) = a4;
    return v_rip + 4769248;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpUsageProviderWorkItemInitialize(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg2 = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    *(uint64_t *)(arg1 + 0x10) = v_rip + 63;
    *(uint64_t *)(arg1 + 0x30) = v_rip + 4769248;
    *(void **)(arg1 + 0x18) = Arg1;
    *(uint64_t *)(arg1) = 0;
    *(uint32_t *)(arg1 + 0x28) = 0;
    *(uint64_t *)(arg1 + 0x20) = 0;
    *(uint32_t *)(arg1 + 0x2C) = 4;
    *(uint64_t *)(arg1 + 0x38) = Arg4;
    return v_rip + 4769248;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `32` | `W` |
| `Arg1` | `+ 0x2C` | `32` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066B4B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066B4B8[BB_0066B4B8]
  bb_0066B4EE[BB_0066B4EE]
```
