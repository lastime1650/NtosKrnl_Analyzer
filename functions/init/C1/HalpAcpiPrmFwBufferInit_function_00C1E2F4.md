# HalpAcpiPrmFwBufferInit

- RVA: `0x00C1E2F4`–`0x00C1E317` (길이 `35` bytes)
- VA: `0x0000000140C1E2F4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpAcpiInitSystem](../../pagelk/B5/HalpAcpiInitSystem_function_00B5D390.md) at `0x00B5D402`

### Static image references
- `0x00C1E302` → RVA `0x01202038` (`CFGRO`; write)
- `0x00C1E30F` → RVA `0x01202030` (`CFGRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1E2F4  48 8B 91 F0 00 00 00            mov rdx, qword ptr [rcx + 0xf0]
00C1E2FB  48 8B 82 38 0F 00 00            mov rax, qword ptr [rdx + 0xf38]
00C1E302  48 89 05 2F 3D 5E 00            mov qword ptr [rip + 0x5e3d2f], rax
00C1E309  8B 82 40 0F 00 00               mov eax, dword ptr [rdx + 0xf40]
00C1E30F  89 05 1B 3D 5E 00               mov dword ptr [rip + 0x5e3d1b], eax
00C1E315  C3                              ret
00C1E316  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAcpiPrmFwBufferInit(__int64 a1)
{
    *(unsigned __int64 *)(v_rip + 6176047) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 3896);
    *(unsigned int *)(v_rip + 6176027) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 3904)));
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 3904));
}
```

## 5. (Beta) C Style

```c
int64_t HalpAcpiPrmFwBufferInit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(v_rip + 0x5E3D2F) = *(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xF38);
    *(uint32_t *)(v_rip + 0x5E3D1B) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xF40)));
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0xF40));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1E2F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1E2F4[BB_00C1E2F4]
  bb_00C1E316[BB_00C1E316]
```
