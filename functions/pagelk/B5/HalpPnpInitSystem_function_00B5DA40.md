# HalpPnpInitSystem

- RVA: `0x00B5DA40`–`0x00B5DA57` (길이 `23` bytes)
- VA: `0x0000000140B5DA40`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B5DA45` → RVA `0x00708000` (`HaliInitPnpDriver`; read)
- `0x00B5DA4C` → RVA `0x00E00690` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B5DA40  83 F9 07                        cmp ecx, 7
00B5DA43  75 0E                           jne 0x140b5da53
00B5DA45  48 8D 05 B4 A5 BA FF            lea rax, [rip - 0x455a4c]
00B5DA4C  48 89 05 3D 2C 2A 00            mov qword ptr [rip + 0x2a2c3d], rax
00B5DA53  33 C0                           xor eax, eax
00B5DA55  C3                              ret
00B5DA56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPnpInitSystem(int a1)
{
    __int64 result;

    if (a1 == 7) {
        result = v_rip - 4545100;
        *(unsigned __int64 *)(v_rip + 2763837) = result;
    }
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpPnpInitSystem(int32_t Arg1)
{
    int64_t result;

    if (Arg1 == 7) {
        result = v_rip - 4545100;
        *(uint64_t *)(v_rip + 0x2A2C3D) = result;
    }
    result = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B5DA40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B5DA40[BB_00B5DA40]
  bb_00B5DA45[BB_00B5DA45]
  bb_00B5DA53[BB_00B5DA53]
  bb_00B5DA56[BB_00B5DA56]
  bb_00B5DA40 -->|branch| bb_00B5DA53
  bb_00B5DA40 -->|fallthrough| bb_00B5DA45
  bb_00B5DA45 -->|flow| bb_00B5DA53
```
