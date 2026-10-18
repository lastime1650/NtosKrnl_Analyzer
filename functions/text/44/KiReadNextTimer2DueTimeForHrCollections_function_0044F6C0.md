# KiReadNextTimer2DueTimeForHrCollections

- RVA: `0x0044F6C0`–`0x0044F6DE` (길이 `30` bytes)
- VA: `0x000000014044F6C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiGetNextTimer2ExpirationDueTime](../5C/KiGetNextTimer2ExpirationDueTime_function_005C644C.md) at `0x005C64D3`

### Static image references
- `0x0044F6C0` → RVA `0x00F23360` (`.data`; read)
- `0x0044F6CB` → RVA `0x00F23348` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044F6C0  48 8B 05 99 3C AD 00            mov rax, qword ptr [rip + 0xad3c99]
0044F6C7  84 C9                           test cl, cl
0044F6C9  74 11                           je 0x14044f6dc
0044F6CB  48 8B 0D 76 3C AD 00            mov rcx, qword ptr [rip + 0xad3c76]
0044F6D2  48 3B C1                        cmp rax, rcx
0044F6D5  48 0F 42 C8                     cmovb rcx, rax
0044F6D9  48 8B C1                        mov rax, rcx
0044F6DC  C3                              ret
0044F6DD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiReadNextTimer2DueTimeForHrCollections(unsigned __int8 a1)
{
    __int64 result;

    result = *(unsigned __int64 *)(v_rip + 11353241);
    if (a1 != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 11353206);
        if ((*(unsigned __int64 *)(v_rip + 11353241)) < a1) { a1 = *(unsigned __int64 *)(v_rip + 11353241); }
        result = a1;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiReadNextTimer2DueTimeForHrCollections(uint8_t Arg1)
{
    int64_t result;

    result = *(uint64_t *)(v_rip + 0xAD3C99);
    if (Arg1 != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xAD3C76);
        if ((*(uint64_t *)(v_rip + 0xAD3C99)) < Arg1) { Arg1 = *(uint64_t *)(v_rip + 0xAD3C99); }
        result = Arg1;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044F6C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044F6C0[BB_0044F6C0]
  bb_0044F6CB[BB_0044F6CB]
  bb_0044F6DC[BB_0044F6DC]
  bb_0044F6DD[BB_0044F6DD]
  bb_0044F6C0 -->|branch| bb_0044F6DC
  bb_0044F6C0 -->|fallthrough| bb_0044F6CB
  bb_0044F6CB -->|flow| bb_0044F6DC
```
