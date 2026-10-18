# MiInitializePageChainPacket

- RVA: `0x004367C0`–`0x004367DF` (길이 `31` bytes)
- VA: `0x00000001404367C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A3020`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3AFA`
- [MiGetHardFaultPages](../36/MiGetHardFaultPages_function_0036200C.md) at `0x00362126`
- [MiResolvePageFileFault](../36/MiResolvePageFileFault_function_0036D968.md) at `0x0036E593`
- [MiInitializePoolPageChainPacket](MiInitializePoolPageChainPacket_function_00436760.md) at `0x004367A7`
- [MiGetClusterPage](../4D/MiGetClusterPage_function_004DC57C.md) at `0x004DC9E5`
- [MiPfPrepareSequentialReadList](../../page/93/MiPfPrepareSequentialReadList_function_0093D8E8.md) at `0x0093DA64`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004367C0  40 53                           push rbx
004367C2  4C 8B 54 24 70                  mov r10, qword ptr [rsp + 0x70]
004367C7  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
004367CB  44 8B 5C 24 38                  mov r11d, dword ptr [rsp + 0x38]
004367D0  41 C1 E0 04                     shl r8d, 4
004367D4  41 8B 42 1C                     mov eax, dword ptr [r10 + 0x1c]
004367D8  44 33 C0                        xor r8d, eax
004367DB  41 83 E0 30                     and r8d, 0x30
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializePageChainPacket(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, unsigned int a10, __int64 a11, __int64 a12, __int64 a13)
{
    a3 = (unsigned int)((a3) << (4));
    a3 = (unsigned int)((a3) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a13 + 28)))));
    a3 = (unsigned int)((a3) & (48));
    return (unsigned int)(*(unsigned int *)(a13 + 28));
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializePageChainPacket(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint32_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint32_t Arg10, uint64_t Arg11, uint64_t Arg12, void *Arg13)
{
    uint8_t *arg13 = (uint8_t *)Arg13;

    Arg3 = (uint32_t)((Arg3) << (4));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(arg13 + 0x1C)))));
    Arg3 = (uint32_t)((Arg3) & (48));
    return (uint32_t)(*(uint32_t *)(arg13 + 0x1C));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg13` | `+ 0x1C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004367C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004367C0[BB_004367C0]
```
