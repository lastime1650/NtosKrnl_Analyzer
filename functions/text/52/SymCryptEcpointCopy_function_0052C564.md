# SymCryptEcpointCopy

- RVA: `0x0052C564`–`0x0052C599` (길이 `53` bytes)
- VA: `0x000000014052C564`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0052C58E` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [SymCryptEcpointMultiScalarMulWnafWithInterleaving](SymCryptEcpointMultiScalarMulWnafWithInterleaving_function_0052B920.md) at `0x0052BC2A`
- [SymCryptEcpointMultiScalarMulWnafWithInterleaving](SymCryptEcpointMultiScalarMulWnafWithInterleaving_function_0052B920.md) at `0x0052BD0D`
- [SymCryptEcpointMultiScalarMulWnafWithInterleaving](SymCryptEcpointMultiScalarMulWnafWithInterleaving_function_0052B920.md) at `0x0052BDF4`
- [SymCryptEcpointScalarMulFixedWindow](SymCryptEcpointScalarMulFixedWindow_function_0052BE30.md) at `0x0052C118`
- [SymCryptEcpointScalarMulFixedWindow](SymCryptEcpointScalarMulFixedWindow_function_0052BE30.md) at `0x0052C416`
- [SymCryptEcpointTransform](SymCryptEcpointTransform_function_0052C9E8.md) at `0x0052CA6D`
- [SymCryptShortWeierstrassAdd](../53/SymCryptShortWeierstrassAdd_function_00537BC0.md) at `0x00537D54`
- [SymCryptShortWeierstrassAddSideChannelUnsafe](../53/SymCryptShortWeierstrassAddSideChannelUnsafe_function_00538188.md) at `0x00538237`
- [SymCryptMontgomerySetDistinguished](../53/SymCryptMontgomerySetDistinguished_function_00539600.md) at `0x0053960E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0052C564  48 83 EC 28                     sub rsp, 0x28
0052C568  4D 8B C8                        mov r9, r8
0052C56B  49 3B D0                        cmp rdx, r8
0052C56E  74 23                           je 0x14052c593
0052C570  8A 02                           mov al, byte ptr [rdx]
0052C572  48 83 C2 20                     add rdx, 0x20
0052C576  41 88 00                        mov byte ptr [r8], al
0052C579  44 8B 41 08                     mov r8d, dword ptr [rcx + 8]
0052C57D  41 83 E0 0F                     and r8d, 0xf
0052C581  44 0F AF 41 10                  imul r8d, dword ptr [rcx + 0x10]
0052C586  49 8D 49 20                     lea rcx, [r9 + 0x20]
0052C58A  41 C1 E0 06                     shl r8d, 6
0052C58E  E8 AD A2 19 00                  call 0x1406c6840
0052C593  48 83 C4 28                     add rsp, 0x28
0052C597  C3                              ret
0052C598  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptEcpointCopy(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != a3) {
        result = *(unsigned __int8 *)(a2);
        a2 = (a2) + (32);
        *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
        a3 = *(unsigned int *)(a1 + 8);
        a3 = (unsigned int)((a3) & (15));
        a3 = (unsigned int)((a3) * (*(unsigned int *)(a1 + 16)));
        a1 = a3 + 32;
        a3 = (unsigned int)((a3) << (6));
        result = memcpy(a1, a2, a3, a3);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptEcpointCopy(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != Arg3) {
        result = *(uint8_t *)(Arg2);
        Arg2 = (Arg2) + (32);
        *(uint8_t *)(arg3) = (uint8_t)(result);
        Arg3 = *(uint32_t *)(arg1 + 0x8);
        Arg3 = (uint32_t)((Arg3) & (15));
        Arg3 = (uint32_t)((Arg3) * (*(uint32_t *)(arg1 + 0x10)));
        Arg1 = Arg3 + 32;
        Arg3 = (uint32_t)((Arg3) << (6));
        result = memcpy(Arg1, Arg2, Arg3, Arg3);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |
| `Arg3` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0052C564&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0052C564[BB_0052C564]
  bb_0052C570[BB_0052C570]
  bb_0052C593[BB_0052C593]
  bb_0052C598[BB_0052C598]
  bb_0052C564 -->|branch| bb_0052C593
  bb_0052C564 -->|fallthrough| bb_0052C570
  bb_0052C570 -->|flow| bb_0052C593
```
