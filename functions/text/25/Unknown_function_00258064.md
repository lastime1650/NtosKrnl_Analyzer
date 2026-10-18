# sub_00258064

- RVA: `0x00258064`–`0x00258083` (길이 `31` bytes)
- VA: `0x0000000140258064`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063D30`
- 디코드: `6`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00258069` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0025807A` → [sub_002580EB](Unknown_function_002580EB.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00258064  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
00258069  48 8D 35 90 7F DA FF            lea rsi, [rip - 0x258070]
00258070  8B 8C 86 F0 55 FC 00            mov ecx, dword ptr [rsi + rax*4 + 0xfc55f0]
00258077  83 F9 07                        cmp ecx, 7
0025807A  75 6F                           jne 0x1402580eb
0025807C  48 8B 83 20 02 00 00            mov rax, qword ptr [rbx + 0x220]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00258064(void)
{
    unsigned __int64 v_stack_p40;

    v_stack_p40 = v_rsi;
    return *(unsigned __int64 *)(v_rbx + 544);
}
```

## 5. (Beta) C Style

```c
void sub_00258064(void)
{
    uint64_t v_stack_p40;

    v_stack_p40 = local_rsi;
    return *(uint64_t *)(local_rbx + 0x220);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00258064&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00258064[BB_00258064]
  bb_0025807C[BB_0025807C]
  bb_00258064 -->|fallthrough| bb_0025807C
```
