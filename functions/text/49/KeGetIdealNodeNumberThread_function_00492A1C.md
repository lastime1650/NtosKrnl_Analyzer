# KeGetIdealNodeNumberThread

- RVA: `0x00492A1C`–`0x00492A3D` (길이 `33` bytes)
- VA: `0x0000000140492A1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MmAllocateNonCachedMemory](../../page/7F/MmAllocateNonCachedMemory_function_007FBB60.md) at `0x007FBBAD`
- [MiCreateHardwareEnclave](../../page/80/MiCreateHardwareEnclave_function_00808500.md) at `0x008086AD`
- [MiAllocateUserPhysicalPages](../../page/80/MiAllocateUserPhysicalPages_function_00809828.md) at `0x00809D47`
- [MmManagePartitionMoveMemory](../../page/80/MmManagePartitionMoveMemory_function_0080E1F4.md) at `0x0080E23F`

### Static image references
- `0x00492A22` → RVA `0x00FC8C40` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00492A1C  8B 81 4C 02 00 00               mov eax, dword ptr [rcx + 0x24c]
00492A22  48 8D 0D 17 62 B3 00            lea rcx, [rip + 0xb36217]
00492A29  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00492A2D  48 8B 80 C0 00 00 00            mov rax, qword ptr [rax + 0xc0]
00492A34  0F B7 80 8A 00 00 00            movzx eax, word ptr [rax + 0x8a]
00492A3B  C3                              ret
00492A3C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGetIdealNodeNumberThread(__int64 a1)
{
    return *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11756055 + (unsigned int)(*(unsigned int *)(a1 + 588)) * 8) + 192) + 138);
}
```

## 5. (Beta) C Style

```c
int64_t KeGetIdealNodeNumberThread(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    return *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB36217 + (uint32_t)(*(uint32_t *)(arg1 + 0x24C)) * 8) + 0xC0) + 0x8A);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00492A1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00492A1C[BB_00492A1C]
  bb_00492A3C[BB_00492A3C]
```
