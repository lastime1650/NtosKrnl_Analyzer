# sub_0033BDE8

- RVA: `0x0033BDE8`–`0x0033BE0B` (길이 `35` bytes)
- VA: `0x000000014033BDE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076EF0`
- 디코드: `9`개 명령, `35/35` bytes 표시
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
- `0x0033BDEE` → RVA `0x00E3D240` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0033BE09` → [sub_0033BCB7 + 0xED](Unknown_function_0033BCB7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0033BDE8  49 8B C7                        mov rax, r15
0033BDEB  48 2B F8                        sub rdi, rax
0033BDEE  48 8B 05 4B 14 B0 00            mov rax, qword ptr [rip + 0xb0144b]
0033BDF5  48 C1 FF 04                     sar rdi, 4
0033BDF9  49 0F AF FC                     imul rdi, r12
0033BDFD  48 C1 EF 09                     shr rdi, 9
0033BE01  0F B6 4C 78 01                  movzx ecx, byte ptr [rax + rdi*2 + 1]
0033BE06  80 E1 7F                        and cl, 0x7f
0033BE09  EB 99                           jmp 0x14033bda4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0033BDE8(void)
{
    __int64 v_rdi;

    v_rdi = (v_rdi) - (v_r15);
    v_rdi = (v_rdi) >> (4);
    v_rdi = (v_rdi) * (v_r12);
    v_rdi = (v_rdi) >> (9);
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 11539531) + v_rdi * 2 + 1)) & (127));
}
```

## 5. (Beta) C Style

```c
void sub_0033BDE8(void)
{
    int64_t local_rdi;

    local_rdi = (local_rdi) - (local_r15);
    local_rdi = (local_rdi) >> (4);
    local_rdi = (local_rdi) * (local_r12);
    local_rdi = (local_rdi) >> (9);
    a1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0xB0144B) + local_rdi * 2 + 0x1)) & (127));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033BDE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033BDE8[BB_0033BDE8]
```
