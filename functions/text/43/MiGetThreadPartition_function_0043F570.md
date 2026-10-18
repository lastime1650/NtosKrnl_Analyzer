# MiGetThreadPartition

- RVA: `0x0043F570`–`0x0043F58B` (길이 `27` bytes)
- VA: `0x000000014043F570`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiResolveMemoryEvent](../../page/A7/MiResolveMemoryEvent_function_00A70A70.md) at `0x00A70A7D`
- [NtSetSystemInformation](../../page/AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF5BB4`

### Static image references
- `0x0043F57E` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043F570  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
0043F577  0F B7 88 AE 04 00 00            movzx ecx, word ptr [rax + 0x4ae]
0043F57E  48 8B 05 03 0B 9F 00            mov rax, qword ptr [rip + 0x9f0b03]
0043F585  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
0043F589  C3                              ret
0043F58A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetThreadPartition(__int64 a1)
{
    return *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10423043) + *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 1198) * 8);
}
```

## 5. (Beta) C Style

```c
int64_t MiGetThreadPartition(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    return *(uint64_t *)(*(uint64_t *)(v_rip + 0x9F0B03) + *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x4AE) * 8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043F570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043F570[BB_0043F570]
  bb_0043F58A[BB_0043F58A]
```
