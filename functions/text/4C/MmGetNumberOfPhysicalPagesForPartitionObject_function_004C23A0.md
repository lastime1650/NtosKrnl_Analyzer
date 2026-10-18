# MmGetNumberOfPhysicalPagesForPartitionObject

- RVA: `0x004C23A0`–`0x004C23BA` (길이 `26` bytes)
- VA: `0x00000001404C23A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcPartitionTelemetryCallback](../../page/A9/CcPartitionTelemetryCallback_function_00A95010.md) at `0x00A95032`

### Static image references
- `0x004C23A6` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C23A0  48 8B 01                        mov rax, qword ptr [rcx]
004C23A3  0F B7 08                        movzx ecx, word ptr [rax]
004C23A6  48 8B 05 DB DC 96 00            mov rax, qword ptr [rip + 0x96dcdb]
004C23AD  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
004C23B1  48 8B 80 50 48 00 00            mov rax, qword ptr [rax + 0x4850]
004C23B8  C3                              ret
004C23B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmGetNumberOfPhysicalPagesForPartitionObject(__int64 a1)
{
    return *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9886939) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1)) * 8) + 18512);
}
```

## 5. (Beta) C Style

```c
int64_t MmGetNumberOfPhysicalPagesForPartitionObject(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    return *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x96DCDB) + *(uint16_t *)(*(uint64_t *)(arg1)) * 8) + 0x4850);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C23A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C23A0[BB_004C23A0]
  bb_004C23B9[BB_004C23B9]
```
