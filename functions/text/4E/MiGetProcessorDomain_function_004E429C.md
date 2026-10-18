# MiGetProcessorDomain

- RVA: `0x004E429C`–`0x004E42B1` (길이 `21` bytes)
- VA: `0x00000001404E429C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInitializeZeroingDomains](../../page/81/MiInitializeZeroingDomains_function_00810884.md) at `0x00810929`

### Static image references
- `0x004E429E` → RVA `0x00FC8C40` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E429C  8B C1                           mov eax, ecx
004E429E  48 8D 0D 9B 49 AE 00            lea rcx, [rip + 0xae499b]
004E42A5  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
004E42A9  8B 80 34 B9 00 00               mov eax, dword ptr [rax + 0xb934]
004E42AF  C3                              ret
004E42B0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetProcessorDomain(int a1)
{
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11422107 + (unsigned int)(a1) * 8) + 47412));
}
```

## 5. (Beta) C Style

```c
int64_t MiGetProcessorDomain(int32_t Arg1)
{
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xAE499B + (uint32_t)(Arg1) * 8) + 0xB934));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E429C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004E429C[BB_004E429C]
  bb_004E42B0[BB_004E42B0]
```
