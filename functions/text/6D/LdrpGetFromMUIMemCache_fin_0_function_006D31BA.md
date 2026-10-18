# LdrpGetFromMUIMemCache$fin$0

- RVA: `0x006D31BA`–`0x006D31E1` (길이 `39` bytes)
- VA: `0x00000001406D31BA`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A7B94`
- 디코드: `13`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006D31D4` → [KeReleaseMutant](../39/KeReleaseMutant_function_003967D0.md) (function, `0x003967D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D31CD` → RVA `0x00F05C60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D31BA  40 55                           push rbp
006D31BC  48 83 EC 30                     sub rsp, 0x30
006D31C0  48 8B EA                        mov rbp, rdx
006D31C3  45 33 C9                        xor r9d, r9d
006D31C6  45 33 C0                        xor r8d, r8d
006D31C9  41 8D 51 01                     lea edx, [r9 + 1]
006D31CD  48 8D 0D 8C 2A 83 00            lea rcx, [rip + 0x832a8c]
006D31D4  E8 F7 35 CC FF                  call 0x1403967d0
006D31D9  90                              nop
006D31DA  48 83 C4 30                     add rsp, 0x30
006D31DE  5D                              pop rbp
006D31DF  C3                              ret
006D31E0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrpGetFromMUIMemCache_fin_0(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    a4 = 0;
    a3 = 0;
    result = KeReleaseMutant(v_rip + 8596108, a4 + 1, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LdrpGetFromMUIMemCache_fin_0(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    Arg4 = 0;
    Arg3 = 0;
    result = KeReleaseMutant(v_rip + 8596108, Arg4 + 1, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D31BA&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D31BA[BB_006D31BA]
  bb_006D31E0[BB_006D31E0]
```
