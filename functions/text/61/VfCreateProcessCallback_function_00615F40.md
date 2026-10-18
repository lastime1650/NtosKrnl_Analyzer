# VfCreateProcessCallback

- RVA: `0x00615F40`–`0x00615F61` (길이 `33` bytes)
- VA: `0x0000000140615F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00615F56` → [ViCreateProcessCallbackInternal](../../pagevrfy/BA/ViCreateProcessCallbackInternal_function_00BA68C0.md) (function, `0x00BA68C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00615F44` → RVA `0x00F04984` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00615F56` → [ViCreateProcessCallbackInternal](../../pagevrfy/BA/ViCreateProcessCallbackInternal_function_00BA68C0.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00615F40  48 83 EC 28                     sub rsp, 0x28
00615F44  83 3D 39 EA 8E 00 00            cmp dword ptr [rip + 0x8eea39], 0
00615F4B  48 8B C2                        mov rax, rdx
00615F4E  74 0B                           je 0x140615f5b
00615F50  41 8A D0                        mov dl, r8b
00615F53  48 8B C8                        mov rcx, rax
00615F56  E8 65 09 59 00                  call 0x140ba68c0
00615F5B  48 83 C4 28                     add rsp, 0x28
00615F5F  C3                              ret
00615F60  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfCreateProcessCallback(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a2;
    if ((*(unsigned int *)(v_rip + 9366073)) != 0) {
        a2 = a3;
        a1 = a2;
        result = ViCreateProcessCallbackInternal(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfCreateProcessCallback(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg2;
    if ((*(uint32_t *)(v_rip + 0x8EEA39)) != 0) {
        Arg2 = Arg3;
        Arg1 = Arg2;
        result = ViCreateProcessCallbackInternal(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00615F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00615F40[BB_00615F40]
  bb_00615F50[BB_00615F50]
  bb_00615F5B[BB_00615F5B]
  bb_00615F60[BB_00615F60]
  bb_00615F40 -->|branch| bb_00615F5B
  bb_00615F40 -->|fallthrough| bb_00615F50
  bb_00615F50 -->|flow| bb_00615F5B
```
