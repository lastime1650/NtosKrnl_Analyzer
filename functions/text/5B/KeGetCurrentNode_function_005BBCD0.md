# KeGetCurrentNode

- RVA: `0x005BBCD0`–`0x005BBCF4` (길이 `36` bytes)
- VA: `0x00000001405BBCD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpPartitionCreatePool](../../page/AF/ExpPartitionCreatePool_function_00AF68A8.md) at `0x00AF68E8`

### Static image references
- `0x005BBCE7` → RVA `0x00FCF6C0` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005BBCD0  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
005BBCD9  48 8B 88 C0 00 00 00            mov rcx, qword ptr [rax + 0xc0]
005BBCE0  0F B7 81 8A 00 00 00            movzx eax, word ptr [rcx + 0x8a]
005BBCE7  48 8D 0D D2 39 A1 00            lea rcx, [rip + 0xa139d2]
005BBCEE  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
005BBCF2  C3                              ret
005BBCF3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGetCurrentNode(void)
{
    return *(unsigned __int64 *)(v_rip + 10566098 + *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 192) + 138) * 8);
}
```

## 5. (Beta) C Style

```c
void KeGetCurrentNode(void)
{
    return *(uint64_t *)(v_rip + 0xA139D2 + *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0xC0) + 0x8A) * 8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005BBCD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005BBCD0[BB_005BBCD0]
  bb_005BBCF3[BB_005BBCF3]
```
