# FsRtlpOplockBreakByCacheFlags$fin$0

- RVA: `0x006D52DB`–`0x006D52EB` (길이 `16` bytes)
- VA: `0x00000001406D52DB`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000C5F2C`
- 디코드: `7`개 명령, `16/16` bytes 표시
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
006D52DB  40 55                           push rbp
006D52DD  48 83 EC 60                     sub rsp, 0x60
006D52E1  48 8B EA                        mov rbp, rdx
006D52E4  48 83 C4 60                     add rsp, 0x60
006D52E8  5D                              pop rbp
006D52E9  C3                              ret
006D52EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall FsRtlpOplockBreakByCacheFlags_fin_0(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (96);
    v_rsp = (v_rsp) + (96);
    return;
}
```

## 5. (Beta) C Style

```c
void FsRtlpOplockBreakByCacheFlags_fin_0(int64_t Arg1, int64_t Arg2)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (96);
    local_rsp = (local_rsp) + (96);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D52DB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D52DB[BB_006D52DB]
  bb_006D52EA[BB_006D52EA]
```
