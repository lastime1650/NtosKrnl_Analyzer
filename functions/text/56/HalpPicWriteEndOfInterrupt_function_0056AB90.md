# HalpPicWriteEndOfInterrupt

- RVA: `0x0056AB90`–`0x0056ABB4` (길이 `36` bytes)
- VA: `0x000000014056AB90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0056ABA9` → [HalpIoDelay](../6A/HalpIoDelay_function_006AC7E0.md) (function, `0x006AC7E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0056AB90  48 83 EC 28                     sub rsp, 0x28
0056AB94  90                              nop
0056AB95  BA A0 00 00 00                  mov edx, 0xa0
0056AB9A  8D 4A 80                        lea ecx, [rdx - 0x80]
0056AB9D  8A C1                           mov al, cl
0056AB9F  EE                              out dx, al
0056ABA0  90                              nop
0056ABA1  8B D1                           mov edx, ecx
0056ABA3  90                              nop
0056ABA4  EE                              out dx, al
0056ABA5  90                              nop
0056ABA6  90                              nop
0056ABA7  EC                              in al, dx
0056ABA8  90                              nop
0056ABA9  E8 32 1C 14 00                  call 0x1406ac7e0
0056ABAE  48 83 C4 28                     add rsp, 0x28
0056ABB2  C3                              ret
0056ABB3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPicWriteEndOfInterrupt(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HalpIoDelay(160 - 128, (unsigned int)((unsigned int)(160 - 128)), a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpPicWriteEndOfInterrupt(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HalpIoDelay(160 - 128, (uint32_t)((uint32_t)(160 - 128)), a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0056AB90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0056AB90[BB_0056AB90]
  bb_0056ABB3[BB_0056ABB3]
```
