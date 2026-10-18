# sub_003F37E3

- RVA: `0x003F37E3`–`0x003F37F9` (길이 `22` bytes)
- VA: `0x00000001403F37E3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000970F0`
- 디코드: `10`개 명령, `22/22` bytes 표시
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
003F37E3  48 85 F6                        test rsi, rsi
003F37E6  74 04                           je 0x1403f37ec
003F37E8  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
003F37EC  48 89 6B 08                     mov qword ptr [rbx + 8], rbp
003F37F0  48 83 C4 30                     add rsp, 0x30
003F37F4  5E                              pop rsi
003F37F5  5D                              pop rbp
003F37F6  5B                              pop rbx
003F37F7  C3                              ret
003F37F8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_003F37E3(void)
{
    __int64 v_rsp;

    if (v_rsi != 0) {
        *(unsigned __int8 *)(v_rsi + 10) = 1;
    }
    *(unsigned __int64 *)(v_rbx + 8) = v_rbp;
    v_rsp = (v_rsp) + (48);
    return;
}
```

## 5. (Beta) C Style

```c
void sub_003F37E3(void)
{
    int64_t local_rsp;

    if (local_rsi != 0) {
        *(uint8_t *)(local_rsi + 0xA) = 1;
    }
    *(uint64_t *)(local_rbx + 0x8) = local_rbp;
    local_rsp = (local_rsp) + (48);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F37E3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F37E3[BB_003F37E3]
  bb_003F37E8[BB_003F37E8]
  bb_003F37EC[BB_003F37EC]
  bb_003F37F8[BB_003F37F8]
  bb_003F37E3 -->|branch| bb_003F37EC
  bb_003F37E3 -->|fallthrough| bb_003F37E8
  bb_003F37E8 -->|flow| bb_003F37EC
```
