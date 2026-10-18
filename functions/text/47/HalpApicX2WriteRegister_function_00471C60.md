# HalpApicX2WriteRegister

- RVA: `0x00471C60`–`0x00471C75` (길이 `21` bytes)
- VA: `0x0000000140471C60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00471C60  C1 F9 04                        sar ecx, 4
00471C63  8B D2                           mov edx, edx
00471C65  81 C1 00 08 00 00               add ecx, 0x800
00471C6B  8B C2                           mov eax, edx
00471C6D  48 C1 EA 20                     shr rdx, 0x20
00471C71  0F 30                           wrmsr
00471C73  C3                              ret
00471C74  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpApicX2WriteRegister(int a1, int a2)
{
    a1 = (unsigned int)((a1) >> (4));
    a1 = (unsigned int)((a1) + (0x800ULL));
    a2 = ((unsigned int)(a2)) >> (32);
    return (unsigned int)((unsigned int)((unsigned int)(a2)));
}
```

## 5. (Beta) C Style

```c
int64_t HalpApicX2WriteRegister(int32_t Arg1, int32_t Arg2)
{
    Arg1 = (uint32_t)((Arg1) >> (4));
    Arg1 = (uint32_t)((Arg1) + (0x800ULL));
    Arg2 = ((uint32_t)(Arg2)) >> (32);
    return (uint32_t)((uint32_t)((uint32_t)(Arg2)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00471C60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00471C60[BB_00471C60]
  bb_00471C74[BB_00471C74]
```
