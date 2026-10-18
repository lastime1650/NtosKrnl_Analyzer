# sub_0088A3C7

- RVA: `0x0088A3C7`–`0x0088A3D5` (길이 `14` bytes)
- VA: `0x000000014088A3C7`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007D0C0`
- 디코드: `6`개 명령, `14/14` bytes 표시
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
0088A3C7  48 83 C4 40                     add rsp, 0x40
0088A3CB  5B                              pop rbx
0088A3CC  C3                              ret
0088A3CD  CC                              int3
0088A3CE  B8 19 00 00 C0                  mov eax, 0xc0000019
0088A3D3  EB F2                           jmp 0x14088a3c7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0088A3C7(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_0088A3C7(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0088A3C7&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0088A3C7[BB_0088A3C7]
  bb_0088A3CD[BB_0088A3CD]
  bb_0088A3CD -->|branch| bb_0088A3C7
```
