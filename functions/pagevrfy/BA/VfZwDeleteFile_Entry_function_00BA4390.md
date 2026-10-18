# VfZwDeleteFile_Entry

- RVA: `0x00BA4390`–`0x00BA43B2` (길이 `34` bytes)
- VA: `0x0000000140BA4390`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA4397` → [ViZwShouldCheck](ViZwShouldCheck_function_00BA4DB4.md) (function, `0x00BA4DB4`)
- `0x00BA43A7` → [ViZwCheckObjectAttributes](ViZwCheckObjectAttributes_function_00BA4C80.md) (function, `0x00BA4C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA4390  48 83 EC 28                     sub rsp, 0x28
00BA4394  4C 8B C1                        mov r8, rcx
00BA4397  E8 18 0A 00 00                  call 0x140ba4db4
00BA439C  85 C0                           test eax, eax
00BA439E  74 0C                           je 0x140ba43ac
00BA43A0  49 8B 10                        mov rdx, qword ptr [r8]
00BA43A3  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
00BA43A7  E8 D4 08 00 00                  call 0x140ba4c80
00BA43AC  48 83 C4 28                     add rsp, 0x28
00BA43B0  C3                              ret
00BA43B1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfZwDeleteFile_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ViZwShouldCheck(a1, a2, a1, a4);
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 8);
        result = ViZwCheckObjectAttributes(a1, a2, a1, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfZwDeleteFile_Entry(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ViZwShouldCheck(Arg1, a2, Arg1, a4);
    if ((uint32_t)(result) != 0) {
        a2 = *(uint64_t *)(Arg1);
        Arg1 = *(uint64_t *)(Arg1 + 0x8);
        result = ViZwCheckObjectAttributes(Arg1, a2, Arg1, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA4390&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA4390[BB_00BA4390]
  bb_00BA43A0[BB_00BA43A0]
  bb_00BA43AC[BB_00BA43AC]
  bb_00BA43B1[BB_00BA43B1]
  bb_00BA4390 -->|branch| bb_00BA43AC
  bb_00BA4390 -->|fallthrough| bb_00BA43A0
  bb_00BA43A0 -->|flow| bb_00BA43AC
```
