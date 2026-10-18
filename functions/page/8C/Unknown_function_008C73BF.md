# sub_008C73BF

- RVA: `0x008C73BF`–`0x008C73D5` (길이 `22` bytes)
- VA: `0x00000001408C73BF`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083D88`
- 디코드: `8`개 명령, `22/22` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008C73CC` → [sub_008C742B](Unknown_function_008C742B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C73BF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
008C73C4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008C73C9  48 3B D8                        cmp rbx, rax
008C73CC  75 5D                           jne 0x1408c742b
008C73CE  48 83 C4 70                     add rsp, 0x70
008C73D2  5B                              pop rbx
008C73D3  C3                              ret
008C73D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008C73BF(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (112);
    return a8;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008C73BF(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, int64_t Arg8)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (112);
    return Arg8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C73BF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C73BF[BB_008C73BF]
  bb_008C73CE[BB_008C73CE]
  bb_008C73D4[BB_008C73D4]
  bb_008C73BF -->|fallthrough| bb_008C73CE
```
